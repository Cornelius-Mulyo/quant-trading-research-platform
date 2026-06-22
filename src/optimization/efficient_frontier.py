import cvxpy as cp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# ======================================
# Database Connection
# ======================================

engine = create_engine(
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

# ======================================
# Assets
# ======================================

tickers = [
    "AAPL",
    "MSFT",
    "NVDA",
    "GOOGL",
    "AMZN"
]

# ======================================
# Load Historical Returns
# ======================================

returns_data = []

for ticker in tickers:

    query = f"""
    SELECT *
    FROM stock_prices
    WHERE ticker='{ticker}'
    ORDER BY date
    """

    df = pd.read_sql(query, engine)

    returns = df["close"].pct_change()

    returns_data.append(
        returns.rename(ticker)
    )

returns_df = pd.concat(
    returns_data,
    axis=1
).dropna()

# ======================================
# Expected Returns & Covariance Matrix
# ======================================

expected_returns = (
    returns_df.mean() * 252
)

cov_matrix = (
    returns_df.cov() * 252
)

n_assets = len(tickers)

# ======================================
# Efficient Frontier
# ======================================

frontier_returns = []
frontier_risks = []

target_returns = np.linspace(
    expected_returns.min(),
    expected_returns.max(),
    50
)

for target in target_returns:

    weights = cp.Variable(n_assets)

    portfolio_return = (
        expected_returns.values @ weights
    )

    portfolio_variance = cp.quad_form(
        weights,
        cov_matrix.values
    )

    constraints = [
        cp.sum(weights) == 1,
        weights >= 0,
        portfolio_return >= target
    ]

    problem = cp.Problem(
        cp.Minimize(portfolio_variance),
        constraints
    )

    problem.solve()

    if weights.value is not None:

        frontier_returns.append(
            portfolio_return.value
        )

        frontier_risks.append(
            np.sqrt(portfolio_variance.value)
        )

# ======================================
# Maximum Sharpe Portfolio
# ======================================

best_sharpe = -999
best_weights = None
best_return = None
best_risk = None

for target in target_returns:

    weights = cp.Variable(n_assets)

    portfolio_return = (
        expected_returns.values @ weights
    )

    portfolio_variance = cp.quad_form(
        weights,
        cov_matrix.values
    )

    constraints = [
        cp.sum(weights) == 1,
        weights >= 0,
        portfolio_return >= target
    ]

    problem = cp.Problem(
        cp.Minimize(portfolio_variance),
        constraints
    )

    problem.solve()

    if weights.value is not None:

        risk = np.sqrt(portfolio_variance.value)

        sharpe = (
            portfolio_return.value / risk
        )

        if sharpe > best_sharpe:

            best_sharpe = sharpe
            best_weights = weights.value
            best_return = portfolio_return.value
            best_risk = risk

# ======================================
# Results
# ======================================

print("\n===== MAXIMUM SHARPE PORTFOLIO =====\n")

for ticker, weight in zip(
        tickers,
        best_weights):

    print(
        f"{ticker}: {weight:.2%}"
    )

print()

print(
    f"Expected Return: "
    f"{best_return:.2%}"
)

print(
    f"Portfolio Risk: "
    f"{best_risk:.2%}"
)

print(
    f"Sharpe Ratio: "
    f"{best_sharpe:.2f}"
)

# ======================================
# Plot Efficient Frontier
# ======================================

plt.figure(figsize=(10, 6))

plt.plot(
    frontier_risks,
    frontier_returns,
    linewidth=2
)

plt.scatter(
    best_risk,
    best_return,
    marker="*",
    s=250
)

plt.xlabel("Portfolio Risk")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "efficient-frontier.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.show()