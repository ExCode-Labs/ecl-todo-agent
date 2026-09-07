from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from todo_agent.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@patch("todo_agent.api.services.ai_service.llm_client")
def test_ai_endpoint(mock_client):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Hello from Gemini!"
    mock_client.chat.completions.create.return_value = mock_response

    response = client.get(
        "/api/v1/ai/test",
        params={
            "prompt": "Say hello in one sentence.",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert isinstance(body["response"], str)
    assert len(body["response"]) > 0
