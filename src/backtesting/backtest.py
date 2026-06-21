import pandas as pd


class Backtester:

    def run(self, df):

        df = df.copy()

        df["returns"] = df["close"].pct_change()

        df["strategy_returns"] = (
            df["signal"].shift(1)
            * df["returns"]
        )

        cumulative_return = (
            1 + df["strategy_returns"]
        ).cumprod()

        total_return = cumulative_return.iloc[-1] - 1

        years = len(df) / 252

        cagr = (
            cumulative_return.iloc[-1]
            ** (1 / years)
        ) - 1

        volatility = (
            df["strategy_returns"].std()
            * (252 ** 0.5)
        )

        sharpe_ratio = (
            cagr / volatility
            if volatility > 0
            else 0
        )

        running_max = cumulative_return.cummax()

        drawdown = (
            cumulative_return - running_max
        ) / running_max

        max_drawdown = drawdown.min()

        return {
            "equity_curve": cumulative_return,
            "total_return": total_return,
            "cagr": cagr,
            "volatility": volatility,
            "sharpe_ratio": sharpe_ratio,
            "max_drawdown": max_drawdown
        }