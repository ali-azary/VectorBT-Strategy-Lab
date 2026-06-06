from pathlib import Path
import argparse
import importlib
import re
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

from vectorbt_strategies.strategy_opt_utils import DEFAULT_INIT_CASH

asset = "BTC-USD"
period = "1y"

INIT_CASH = DEFAULT_INIT_CASH
CORE_MODULES = {
    "__init__",
    "strategy_opt_utils",
    "strategy_registry",
    "strategy_dispatcher",
}


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("_")


def flatten_yfinance_columns(data: pd.DataFrame) -> pd.DataFrame:
    if isinstance(data.columns, pd.MultiIndex):
        if len(data.columns.get_level_values(1).unique()) == 1:
            data = data.droplevel(1, axis=1)
        elif len(data.columns.get_level_values(0).unique()) == 1:
            data = data.droplevel(0, axis=1)
    return data


def download_ohlcv(symbol: str, period: str, interval: str) -> pd.DataFrame:
    data = yf.download(symbol, period=period, interval=interval, auto_adjust=False, progress=False)
    data = flatten_yfinance_columns(data)
    if data.empty:
        raise ValueError(f"No data returned for {symbol}")

    data = data.dropna(subset=["Close"]).copy()
    close = data["Close"].astype(float)
    data["Open"] = data.get("Open", close.shift(1)).reindex(close.index).fillna(close.shift(1)).fillna(close).astype(float)
    data["High"] = data.get("High", close).reindex(close.index).fillna(close).astype(float)
    data["Low"] = data.get("Low", close).reindex(close.index).fillna(close).astype(float)
    data["Close"] = close
    if "Volume" in data.columns:
        data["Volume"] = data["Volume"].reindex(close.index).fillna(0).astype(float)
    else:
        data["Volume"] = 0.0
    return data[["Open", "High", "Low", "Close", "Volume"]]


def buy_and_hold_equity(data: pd.DataFrame) -> pd.Series:
    close = data["Close"].astype(float).dropna()
    if close.empty:
        raise ValueError("Cannot build buy-and-hold benchmark from empty Close data")
    return (INIT_CASH * close / close.iloc[0]).rename("Buy and Hold")


def save_equity_plot(result, output_dir: Path, symbol: str, period: str, benchmark_equity: pd.Series) -> Path:
    portfolio = result.best_portfolio
    strategy_equity = portfolio.value()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(strategy_equity.index, strategy_equity.values, label="Optimized Strategy", linewidth=2.5)
    ax.plot(benchmark_equity.index, benchmark_equity.values, label="Buy and Hold", linestyle="--", linewidth=2.2)
    ax.set_title(f"{symbol} {period} - {result.name}")
    ax.set_ylabel("Portfolio Value")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    path = output_dir / f"{safe_name(result.name)}_equity_vs_buy_hold.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path


def discover_strategy_modules():
    strategy_dir = Path(__file__).resolve().parent / "vectorbt_strategies"
    modules = []
    for path in sorted(strategy_dir.glob("*.py")):
        if path.stem in CORE_MODULES:
            continue
        modules.append(importlib.import_module(f"vectorbt_strategies.{path.stem}"))
    return modules


def main() -> None:
    parser = argparse.ArgumentParser(description="Backtest all clean vectorbt strategy optimizers on one downloaded asset dataset.")
    parser.add_argument("--symbol", default=f"{asset}")
    parser.add_argument("--period", default=f"{period}")
    parser.add_argument("--interval", default="1d")
    args = parser.parse_args()

    folder_name = f"{safe_name(args.symbol)}-{safe_name(args.period)}"
    output_dir = Path(folder_name)
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(exist_ok=True)
    per_strategy_dir = output_dir / "per_strategy_results"
    per_strategy_dir.mkdir(exist_ok=True)

    print(f"Downloading {args.symbol} for {args.period} at {args.interval}...")
    data = download_ohlcv(args.symbol, args.period, args.interval)
    benchmark_equity = buy_and_hold_equity(data)
    benchmark_return_pct = (benchmark_equity.iloc[-1] / benchmark_equity.iloc[0] - 1) * 100
    data.to_csv(output_dir / "data.csv")
    benchmark_equity.to_csv(output_dir / "buy_and_hold_equity.csv", header=True)
    strategy_modules = discover_strategy_modules()

    summary_rows = []
    failures = []

    for module in strategy_modules:
        strategy_name = getattr(module, "STRATEGY_NAME", module.__name__.split(".")[-1])
        print(f"Backtesting {strategy_name}...")
        try:
            result = module.optimize_strategy(data, optimize_for="total_return_pct")
            result.results["init_cash"] = INIT_CASH
            result.results["benchmark_return_pct"] = benchmark_return_pct
            result.results.to_csv(per_strategy_dir / f"{safe_name(result.name)}_optimization_results.csv", index=False)
            plot_path = save_equity_plot(result, output_dir, args.symbol, args.period, benchmark_equity)
            best_row = result.results.iloc[0].to_dict()
            summary_rows.append(
                {
                    "strategy": result.name,
                    "plot": str(plot_path),
                    "init_cash": INIT_CASH,
                    **{f"best_{key}": value for key, value in result.best_params.items()},
                    "total_return_pct": best_row.get("total_return_pct"),
                    "benchmark_return_pct": benchmark_return_pct,
                    "sharpe": best_row.get("sharpe"),
                    "rank_score": best_row.get("_rank_score"),
                    "max_drawdown_pct": best_row.get("max_drawdown_pct"),
                    "total_trades": best_row.get("total_trades"),
                    "end_value": best_row.get("end_value"),
                }
            )
        except Exception as exc:
            failures.append({"strategy": strategy_name, "error": str(exc)})
            print(f"FAILED {strategy_name}: {exc}")

    summary = pd.DataFrame(summary_rows)
    if not summary.empty:
        summary = summary.sort_values("total_return_pct", ascending=False, na_position="last")
    summary.to_csv(output_dir / "summary.csv", index=False)
    pd.DataFrame(failures, columns=["strategy", "error"]).to_csv(output_dir / "failures.csv", index=False)

    print(f"\nSaved backtest folder: {output_dir.resolve()}")
    print(f"Strategies completed: {len(summary_rows)}")
    print(f"Strategies failed: {len(failures)}")
    if not summary.empty:
        print("\nTop strategies by total return:")
        print(summary[["strategy", "total_return_pct", "benchmark_return_pct", "sharpe", "max_drawdown_pct", "total_trades"]].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
