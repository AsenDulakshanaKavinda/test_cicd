from fastapi.testclient import TestClient
# If main.py is in the root, this works when running from the root
from main import app 

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"result": "API running..."}