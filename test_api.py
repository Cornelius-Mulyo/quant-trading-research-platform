from fastapi.testclient import TestClient
import pytest

from src.api.app import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Quantitative Portfolio Research Platform API"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "running"
    }


@pytest.mark.skip(reason="Requires local PostgreSQL database")
def test_portfolio_backtest():
    response = client.get("/portfolio/backtest")

    assert response.status_code == 200

    data = response.json()

    assert "portfolio_return" in data
    assert "cagr" in data
    assert "volatility" in data
    assert "sharpe" in data
    assert "max_drawdown" in data
    assert "final_equity" in data