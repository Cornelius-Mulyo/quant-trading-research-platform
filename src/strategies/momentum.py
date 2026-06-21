import pandas as pd


class MomentumStrategy:

    def __init__(self, window=50):

        self.window = window

    def generate_signals(self, df):

        df = df.copy()

        df["momentum"] = (
            df["close"] /
            df["close"].shift(self.window)
        ) - 1

        df["signal"] = 0

        df.loc[
            df["momentum"] > 0.05,
            "signal"
        ] = 1

        return df