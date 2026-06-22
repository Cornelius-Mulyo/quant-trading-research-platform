# Quantitative Trading Research Platform

A quantitative research platform for developing, backtesting, and optimizing systematic trading strategies using historical market data.

## Overview

This project provides an end-to-end workflow for quantitative strategy research:

* Historical market data ingestion
* PostgreSQL-based data storage
* Momentum-based trading signal generation
* Strategy backtesting
* Performance analytics
* Portfolio construction
* Parameter optimization
* Efficient frontier analysis

The platform was developed to explore how systematic trading strategies perform across multiple technology equities and to evaluate portfolio risk-return tradeoffs.

---

## Technologies

* Python
* PostgreSQL
* Pandas
* NumPy
* SQLAlchemy
* Matplotlib
* yFinance

---

## Project Architecture

```text
Market Data
    ↓
Data Ingestion
    ↓
PostgreSQL Database
    ↓
Trading Strategies
    ↓
Backtesting Engine
    ↓
Performance Analytics
    ↓
Portfolio Optimization
    ↓
Efficient Frontier Visualization
```

---

## Data Universe

The project currently analyzes:

* AAPL (Apple)
* MSFT (Microsoft)
* NVDA (NVIDIA)
* GOOGL (Alphabet)
* AMZN (Amazon)

Historical daily price data is downloaded using Yahoo Finance and stored in PostgreSQL for analysis.

---

## Trading Strategy

### Momentum Strategy

The implemented momentum strategy calculates:

```python
momentum = (close / close.shift(window)) - 1
```

Trading rule:

* Long position when momentum exceeds a threshold
* Flat otherwise

Parameter optimization was performed across multiple lookback windows to identify the strongest risk-adjusted performance.

---

## Backtesting Engine

The custom backtesting engine evaluates:

* Total Return
* CAGR
* Annualized Volatility
* Sharpe Ratio
* Maximum Drawdown

Performance is computed using daily strategy returns and compounded portfolio growth.

---

## Sample Results

### Single-Asset Momentum Strategy (AAPL)

| Metric       | Result  |
| ------------ | ------- |
| CAGR         | 19.38%  |
| Sharpe Ratio | 1.01    |
| Max Drawdown | -20.38% |

### Equal-Weight Portfolio

| Metric       | Result  |
| ------------ | ------- |
| Total Return | 140.95% |
| CAGR         | 19.26%  |
| Volatility   | 16.42%  |
| Sharpe Ratio | 1.17    |
| Max Drawdown | -21.25% |

The portfolio achieved a higher Sharpe Ratio than the individual AAPL strategy, demonstrating diversification benefits and improved risk-adjusted performance.

---

## Portfolio Optimization

The platform includes:

* Multi-asset portfolio construction
* Equal-weight portfolio analysis
* Efficient frontier generation
* Maximum Sharpe portfolio selection

Example output:

```text
Maximum Sharpe Portfolio

AAPL: 1.96%
MSFT: 8.03%
NVDA: 91.82%
GOOGL: 0.00%
AMZN: 0.00%

Expected Return: 74.40%
Portfolio Risk: 50.75%
Sharpe Ratio: 1.43
```

---

## Repository Structure

```text
src/
├── ingestion/
│   ├── download_prices.py
│   └── load_prices.py
│
├── database/
│   └── db_connection.py
│
├── strategies/
│   └── momentum.py
│
├── backtesting/
│   └── backtest.py
│
├── optimization/
│   ├── benchmark_comparison.py
│   ├── parameter_optimization.py
│   ├── multi_stock_analysis.py
│   ├── portfolio_backtest.py
│   └── efficient_frontier.py
```

---

## Future Enhancements

Planned improvements include:

* Additional factor models
* Mean reversion strategies
* Transaction cost modeling
* Position sizing frameworks
* Risk parity portfolios
* Interactive Streamlit dashboard
* Machine learning signal generation

---

## Author

Cornelius Mulyokela

Computer Science & Applied Mathematics

Stetson University
