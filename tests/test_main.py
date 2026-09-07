from fastapi.testclient import TestClient

from todo_agent.config.settings import settings
from todo_agent.main import app

client = TestClient(app)


def test_welcome() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": settings.app_name,
    }
