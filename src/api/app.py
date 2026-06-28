from fastapi import FastAPI

from src.optimization.portfolio_backtest import run_portfolio_backtest

app = FastAPI(
    title="Quantitative Portfolio Research Platform",
    version="1.0.0",
    description="REST API for portfolio optimization, backtesting and quantitative analytics."
)

@app.get("/")
def home():
    return {
        "message": "Quantitative Portfolio Research Platform API"
    }

@app.get("/health")
def health():
    return {
        "status": "running"
    }

@app.get("/portfolio/backtest")
def portfolio_backtest():
    return run_portfolio_backtest()