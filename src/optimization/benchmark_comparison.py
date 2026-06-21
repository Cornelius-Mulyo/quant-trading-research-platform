import pandas as pd
from sqlalchemy import create_engine

from src.strategies.momentum import MomentumStrategy
from src.backtesting.backtest import Backtester


engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

query = """
SELECT *
FROM stock_prices
WHERE ticker='AAPL'
ORDER BY date
"""

df = pd.read_sql(query, engine)

strategy = MomentumStrategy(window=50)

df = strategy.generate_signals(df)

backtester = Backtester()

results = backtester.run(df)

buy_hold_return = (
    df["close"].iloc[-1]
    / df["close"].iloc[0]
) - 1

print("Buy and Hold:")
print(f"{buy_hold_return:.2%}")

print("\nMomentum Strategy:")
print(f"{results['total_return']:.2%}")