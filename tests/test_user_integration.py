from fastapi.testclient import TestClient

def test_create_user_integration(client: TestClient):
    payload = {
        "email": "test@example.com"
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["email"] == "test@example.com"
