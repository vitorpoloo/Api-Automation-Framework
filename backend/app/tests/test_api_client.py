from app.clients.api_client import APIClient


def test_get_request():
    client = APIClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/1")

    assert response.status_code == 200