# Quantitative Portfolio Research Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Pytest](https://img.shields.io/badge/Tested-Pytest-success)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

A production-style quantitative portfolio research platform for developing, backtesting, optimizing, and serving systematic trading strategies using historical market data.

---

# Overview

This project combines quantitative finance with modern backend software engineering practices to provide an end-to-end workflow for portfolio research.

The platform enables users to:

- Ingest historical market data
- Store financial data in PostgreSQL
- Develop systematic trading strategies
- Backtest investment portfolios
- Optimize asset allocations
- Evaluate portfolio performance
- Serve quantitative analytics through a FastAPI REST API
- Automatically validate code through GitHub Actions

---

# Project Highlights

- Built a production-style backend using FastAPI
- Designed a custom portfolio backtesting engine
- Implemented portfolio optimization and Efficient Frontier analysis
- Containerized the application using Docker and Docker Compose
- Added automated API testing using Pytest
- Configured Continuous Integration with GitHub Actions
- Integrated PostgreSQL for persistent market data storage
- Documented REST endpoints using Swagger/OpenAPI

---

# Features

- Historical market data ingestion
- PostgreSQL-backed market data storage
- Momentum-based trading strategy
- Portfolio backtesting engine
- Portfolio performance analytics
- Multi-asset portfolio construction
- Portfolio parameter optimization
- Efficient Frontier generation
- FastAPI REST API
- Interactive Swagger/OpenAPI documentation
- Dockerized deployment
- Automated API testing with Pytest
- Continuous Integration using GitHub Actions

---

# Technologies

## Backend

- Python
- FastAPI
- REST APIs

## Database

- PostgreSQL
- SQLAlchemy

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- Pytest

## Market Data

- Yahoo Finance (yFinance)

---

# Project Architecture

```text
                 Historical Market Data
                          │
                          ▼
                  Data Ingestion Pipeline
                          │
                          ▼
                 PostgreSQL Database
                          │
                          ▼
                 Trading Strategies
                          │
                          ▼
                 Backtesting Engine
                          │
                          ▼
                Portfolio Analytics
                          │
                          ▼
             Portfolio Optimization
                          │
                          ▼
                 FastAPI REST API
                          │
                          ▼
             Swagger Documentation
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Cornelius-Mulyo/quant-trading-research-platform.git

cd quant-trading-research-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn src.api.app:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Run the automated tests:

```bash
pytest
```

---

# Docker

The project can be started entirely with Docker.

Build the containers:

```bash
docker compose build
```

Start the application:

```bash
docker compose up
```

This launches:

- PostgreSQL
- FastAPI API

After startup, open:

```text
http://localhost:8000/docs
```

to access the Swagger UI.

---

# Data Universe

The platform currently analyzes the following technology stocks:

- AAPL (Apple)
- MSFT (Microsoft)
- NVDA (NVIDIA)
- GOOGL (Alphabet)
- AMZN (Amazon)

Historical daily market data is downloaded from Yahoo Finance and stored in PostgreSQL for quantitative analysis.

---

# Trading Strategy

## Momentum Strategy

The implemented momentum strategy calculates:

```python
momentum = (close / close.shift(window)) - 1
```

Trading rules:

- Enter a long position when momentum exceeds a threshold.
- Exit the position when momentum falls below the threshold.

Parameter optimization is performed across multiple lookback windows to maximize risk-adjusted performance.

---

# Backtesting Engine

The custom portfolio backtesting engine evaluates:

- Total Return
- Compound Annual Growth Rate (CAGR)
- Annualized Volatility
- Sharpe Ratio
- Maximum Drawdown

Portfolio performance is calculated using daily strategy returns and compounded portfolio growth.

---

# Sample Results

## Single-Asset Momentum Strategy (AAPL)

| Metric | Result |
|---------|--------|
| CAGR | 19.38% |
| Sharpe Ratio | 1.01 |
| Maximum Drawdown | -20.38% |

---

## Equal-Weight Portfolio

| Metric | Result |
|---------|--------|
| Total Return | 140.95% |
| CAGR | 19.26% |
| Volatility | 16.42% |
| Sharpe Ratio | 1.17 |
| Maximum Drawdown | -21.25% |

The equal-weight portfolio achieved a higher Sharpe Ratio than the individual AAPL strategy, demonstrating improved diversification and stronger risk-adjusted performance.

---

# Portfolio Optimization

The platform supports:

- Multi-asset portfolio construction
- Equal-weight portfolio analysis
- Efficient Frontier generation
- Maximum Sharpe portfolio optimization

Example output:

```text
Maximum Sharpe Portfolio

AAPL:   1.96%
MSFT:   8.03%
NVDA:  91.82%
GOOGL:  0.00%
AMZN:   0.00%

Expected Return: 74.40%
Portfolio Risk: 50.75%
Sharpe Ratio: 1.43
```

---

# REST API

The platform exposes quantitative analytics through a FastAPI backend.

## Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | API Home |
| `/health` | Health Check |
| `/portfolio/backtest` | Execute portfolio backtest and return performance metrics |

Interactive API documentation is automatically generated by FastAPI.

After starting the server, visit:

```text
http://127.0.0.1:8000/docs
```

Example API response:

```json
{
  "portfolio_return": 140.95,
  "cagr": 19.26,
  "volatility": 16.42,
  "sharpe": 1.17,
  "max_drawdown": -21.25,
  "final_equity": 2.4095
}
```

---

# Automated Testing & Continuous Integration

The project includes automated testing and continuous integration to improve reliability and maintain code quality.

## Unit Tests

API endpoints are tested using Pytest and FastAPI's TestClient.

Current automated tests include:

- Home endpoint
- Health endpoint
- Portfolio backtest endpoint (executed locally with a PostgreSQL instance)

Run tests locally:

```bash
pytest
```

## Continuous Integration

GitHub Actions automatically:

- Installs project dependencies
- Runs the automated test suite
- Validates every push and pull request

This ensures the application remains stable as new features are added.

---

# Repository Structure

```text
quant_trading_research_platform/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   ├── api/
│   │   └── app.py
│   │
│   ├── ingestion/
│   │   ├── download_prices.py
│   │   └── load_prices.py
│   │
│   ├── database/
│   │   └── db_connection.py
│   │
│   ├── strategies/
│   │   └── momentum.py
│   │
│   ├── backtesting/
│   │   └── backtest.py
│   │
│   └── optimization/
│       ├── portfolio_backtest.py
│       ├── efficient_frontier.py
│       ├── benchmark_comparison.py
│       ├── parameter_optimization.py
│       └── multi_stock_analysis.py
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Future Enhancements

Planned improvements include:

- JWT Authentication
- OAuth integration
- Redis caching
- Celery background task processing
- Transaction cost modeling
- Position sizing framework
- Risk parity portfolios
- Interactive Streamlit dashboard
- Machine learning trading signals

---

