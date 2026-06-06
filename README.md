# VectorBT-Strategy-Lab
Batch-test strategies across any asset.

I built a script that backtests an entire strategy library automatically.

Testing one strategy is useful.

Testing an entire folder of strategies is where things get interesting.

I’ve been working on a VectorBT strategy lab where each strategy lives as its own module, and I wanted one script that could:

```text
Download market data
Clean the OHLCV dataframe
Discover every strategy module automatically
Run each strategy optimizer
Compare each result against buy-and-hold
Save per-strategy optimization CSVs
Export equity-vs-benchmark charts
Record failures without stopping the run
Create a final ranked summary
```

The interesting part is automatic module discovery.

Instead of manually importing every strategy file, the script scans the strategy folder:

```python
def discover_strategy_modules():
    strategy_dir = Path(__file__).resolve().parent / "vectorbt_strategies"
    modules = []

    for path in sorted(strategy_dir.glob("*.py")):
        if path.stem in CORE_MODULES:
            continue

        modules.append(importlib.import_module(f"vectorbt_strategies.{path.stem}"))

    return modules
```

So if I add a new strategy file to `vectorbt_strategies`, it can automatically become part of the research run.

Each strategy module is expected to expose an optimizer:

```python
result = module.optimize_strategy(data, optimize_for="total_return_pct")
```

Then the script saves the optimization results:

```python
result.results["init_cash"] = INIT_CASH
result.results["benchmark_return_pct"] = benchmark_return_pct

result.results.to_csv(
    per_strategy_dir / f"{safe_name(result.name)}_optimization_results.csv",
    index=False
)
```

I also wanted every strategy compared to buy-and-hold, not just judged in isolation:

```python
def buy_and_hold_equity(data: pd.DataFrame) -> pd.Series:
    close = data["Close"].astype(float).dropna()

    if close.empty:
        raise ValueError("Cannot build buy-and-hold benchmark from empty Close data")

    return (INIT_CASH * close / close.iloc[0]).rename("Buy and Hold")
```

Then each completed strategy gets an equity chart:

```python
ax.plot(strategy_equity.index, strategy_equity.values, label="Optimized Strategy", linewidth=2.5)
ax.plot(benchmark_equity.index, benchmark_equity.values, label="Buy and Hold", linestyle="--", linewidth=2.2)
```

The final summary keeps the useful comparison fields:

```python
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
```

And if one strategy fails, the whole run does not crash:

```python
except Exception as exc:
    failures.append({"strategy": strategy_name, "error": str(exc)})
    print(f"FAILED {strategy_name}: {exc}")
```

At the end, I get:

```text
data.csv
buy_and_hold_equity.csv
summary.csv
failures.csv
per-strategy optimization CSVs
equity-vs-buy-and-hold charts
```

The goal is not to pretend every strategy is good.

It is the opposite.

I want to run the whole library, see what fails, see what survives, compare everything against buy-and-hold, and focus only on candidates worth deeper research.

I packaged the larger workflow here if anyone wants to try it:

https://www.pyquantlab.com/downloads/VectorBT%20Strategy%20Lab.php

Curious how others are organizing multi-strategy backtesting workflows.
