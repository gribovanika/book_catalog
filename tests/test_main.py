from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Book Catalog API"}

def test_register_and_login():
    unique_email = f"user_{uuid.uuid4().hex}@example.com"
    response = client.post("/register/", json={"email": unique_email, "password": "testpass"})
    if response.status_code != 200:
        print("Response status:", response.status_code)
        print("Response body:", response.text)
    assert response.status_code == 200

    response = client.post("/token", data={"username": unique_email, "password": "testpass"})
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data