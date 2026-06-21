import pandas as pd
from sqlalchemy import create_engine

from src.strategies.momentum import MomentumStrategy
from src.backtesting.backtest import Backtester

engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

windows = [5, 10, 20, 50, 100]

results = []

query = """
SELECT *
FROM stock_prices
WHERE ticker='AAPL'
ORDER BY date
"""

df = pd.read_sql(query, engine)

for window in windows:

    strategy = MomentumStrategy(window=window)

    test_df = strategy.generate_signals(df.copy())

    backtester = Backtester()

    metrics = backtester.run(test_df)

    results.append({
        "Window": window,
        "CAGR": metrics["cagr"],
        "Sharpe": metrics["sharpe_ratio"],
        "Drawdown": metrics["max_drawdown"]
    })

results_df = pd.DataFrame(results)

print(results_df)