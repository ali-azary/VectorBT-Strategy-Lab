@echo off
set period=1y
set interval=1d

for %%S in (
SPY QQQ DIA IWM EEM EFA
AAPL MSFT NVDA TSLA AMZN META
BTC-USD ETH-USD SOL-USD BNB-USD XRP-USD ADA-USD
EURUSD=X GBPUSD=X JPY=X CHF=X AUDUSD=X CAD=X
GC=F SI=F CL=F BZ=F NG=F HG=F
TLT IEF SHY HYG LQD AGG
VIXY GLD SLV VNQ XLU XLF
) do (
    echo ======================================
    echo Running backtest for %%S
    echo ======================================
    python backtest_all_strategies.py --symbol %%S --period %period% --interval %interval%
)

echo Batch backtesting complete.
pause