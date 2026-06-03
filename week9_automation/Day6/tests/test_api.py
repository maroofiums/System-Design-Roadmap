from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():

    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "predicted_class" in response.json()

    assert response.json()["predicted_class"] == 0  # Assuming class 0 corresponds to the given features
    assert isinstance(response.json()["predicted_class"], int)

    