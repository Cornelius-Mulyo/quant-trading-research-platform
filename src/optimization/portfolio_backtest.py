import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

from src.strategies.momentum import MomentumStrategy

# Database connection
engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

# Portfolio stocks
tickers = [
    "AAPL",
    "MSFT",
    "NVDA",
    "GOOGL",
    "AMZN"
]

portfolio_returns = []

for ticker in tickers:

    query = f"""
    SELECT *
    FROM stock_prices
    WHERE ticker='{ticker}'
    ORDER BY date
    """

    df = pd.read_sql(query, engine)

    # Generate signals
    strategy = MomentumStrategy(window=50)

    df = strategy.generate_signals(df)

    # Daily returns
    df["returns"] = df["close"].pct_change()

    # Strategy returns
    df["strategy_returns"] = (
        df["signal"].shift(1)
        * df["returns"]
    )

    portfolio_returns.append(
        df["strategy_returns"]
    )

# Combine all stock returns
portfolio = pd.concat(
    portfolio_returns,
    axis=1
)

# Equal-weight portfolio
portfolio["portfolio_return"] = (
    portfolio.mean(axis=1)
)

# Equity curve
equity_curve = (
    1 + portfolio["portfolio_return"]
).cumprod()

# ======================
# Portfolio Statistics
# ======================

total_return = equity_curve.iloc[-1] - 1

years = len(portfolio) / 252

cagr = (
    equity_curve.iloc[-1]
    ** (1 / years)
) - 1

volatility = (
    portfolio["portfolio_return"].std()
    * (252 ** 0.5)
)

sharpe = cagr / volatility

running_max = equity_curve.cummax()

drawdown = (
    equity_curve - running_max
) / running_max

max_drawdown = drawdown.min()

# ======================
# Results
# ======================

print("\n===== PORTFOLIO RESULTS =====")

print(f"Portfolio Return: {total_return:.2%}")
print(f"Portfolio CAGR: {cagr:.2%}")
print(f"Portfolio Volatility: {volatility:.2%}")
print(f"Portfolio Sharpe: {sharpe:.2f}")
print(f"Portfolio Max Drawdown: {max_drawdown:.2%}")

print("\nFinal Equity Value:")
print(f"{equity_curve.iloc[-1]:.4f}")

# ======================
# Plot
# ======================

equity_curve.plot()

plt.title("Equal Weight Momentum Portfolio")
plt.xlabel("Trading Days")
plt.ylabel("Portfolio Value")

plt.show()