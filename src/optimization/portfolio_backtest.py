import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

from src.strategies.momentum import MomentumStrategy

engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)


def run_portfolio_backtest():

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

        strategy = MomentumStrategy(window=50)

        df = strategy.generate_signals(df)

        df["returns"] = df["close"].pct_change()

        df["strategy_returns"] = (
            df["signal"].shift(1)
            * df["returns"]
        )

        portfolio_returns.append(df["strategy_returns"])

    portfolio = pd.concat(
        portfolio_returns,
        axis=1
    )

    portfolio["portfolio_return"] = portfolio.mean(axis=1)

    equity_curve = (
        1 + portfolio["portfolio_return"]
    ).cumprod()

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

    return {
        "portfolio_return": round(total_return * 100, 2),
        "cagr": round(cagr * 100, 2),
        "volatility": round(volatility * 100, 2),
        "sharpe": round(sharpe, 2),
        "max_drawdown": round(max_drawdown * 100, 2),
        "final_equity": round(equity_curve.iloc[-1], 4)
    }


if __name__ == "__main__":
    results = run_portfolio_backtest()

    print(results)