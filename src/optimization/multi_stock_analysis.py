import pandas as pd
from sqlalchemy import create_engine

from src.strategies.momentum import MomentumStrategy
from src.backtesting.backtest import Backtester

engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

tickers = [
    "AAPL",
    "MSFT",
    "NVDA",
    "GOOGL",
    "AMZN"
]

results_table = []

for ticker in tickers:

    query = f"""
    SELECT *
    FROM stock_prices
    WHERE ticker='{ticker}'
    ORDER BY date
    """

    df = pd.read_sql(query, engine)

    strategy = MomentumStrategy()
    df = strategy.generate_signals(df)

    backtester = Backtester()
    results = backtester.run(df)

    results_table.append({
        "Ticker": ticker,
        "CAGR": results["cagr"],
        "Sharpe": results["sharpe_ratio"],
        "Drawdown": results["max_drawdown"]
    })

results_df = pd.DataFrame(results_table)

print(results_df)