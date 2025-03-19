from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}


def test_read_search():
    response = client.get("/search/Python")
    assert response.status_code == 200
    assert "Python" in response.json()["message"]


def test_read_wiki():
    response = client.get("/wiki/Python/2")
    assert response.status_code == 200
    assert "Python" in response.json()["message"]
    response = client.get("/wiki/Python/2")
    assert response.status_code == 200


def test_read_phrase():
    response = client.get("/phrase/Python")
    assert response.status_code == 200
    assert ["python"] == response.json()["message"]
