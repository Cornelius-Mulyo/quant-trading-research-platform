import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

stocks = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]

for symbol in stocks:

    print(f"Loading {symbol}...")

    df = yf.download(
        symbol,
        start="2020-01-01",
        end="2025-01-01",
        progress=False,
        auto_adjust=False
    )

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Keep only columns matching our table
    df = df[["Open", "High", "Low", "Close", "Volume"]]

    # Convert names to lowercase
    df.columns = ["open", "high", "low", "close", "volume"]

    # Add ticker column
    df["ticker"] = symbol

    # Move index into a date column
    df.reset_index(inplace=True)

    # Rename Date column
    df.rename(columns={"Date": "date"}, inplace=True)

    # Insert into PostgreSQL
    df.to_sql(
        "stock_prices",
        engine,
        if_exists="append",
        index=False
    )

    print(f"{symbol} loaded.")

print("Finished loading all stocks.")