from main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

def test_health_success():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
            "message": "API running"
        }