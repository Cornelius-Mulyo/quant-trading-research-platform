import yfinance as yf

stocks = [
    "AAPL",
    "MSFT",
    "NVDA",
    "GOOGL",
    "AMZN"
]

for symbol in stocks:

    df = yf.download(
        symbol,
        start="2020-01-01",
        end="2025-01-01"
    )

    print(f"\n{symbol}")
    print(df.head())