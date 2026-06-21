import matplotlib.pyplot as plt
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

strategy = MomentumStrategy()
df = strategy.generate_signals(df)

backtester = Backtester()
results = backtester.run(df)

print(f"Total Return: {results['total_return']:.2%}")
print(f"CAGR: {results['cagr']:.2%}")
print(f"Volatility: {results['volatility']:.2%}")
print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
print(f"Max Drawdown: {results['max_drawdown']:.2%}")

print("\nEquity Curve:")
print(results["equity_curve"].tail())

results["equity_curve"].plot()
plt.title("Momentum Strategy Equity Curve")
plt.xlabel("Trading Days")
plt.ylabel("Portfolio Value")
plt.show()
