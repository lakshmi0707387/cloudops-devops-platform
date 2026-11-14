
import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"CloudOps Health Monitor" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_version_endpoint(client):
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"


def test_environment_endpoint(client):
    response = client.get("/environment")

    assert response.status_code == 200
    assert response.json["environment"] == "development"
