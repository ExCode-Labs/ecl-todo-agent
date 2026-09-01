from fastapi.testclient import TestClient

from todo_agent.main import app

client = TestClient(app)


def test_welcome() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Todo Agent API",
    }
