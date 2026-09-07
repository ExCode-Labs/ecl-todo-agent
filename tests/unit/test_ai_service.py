from unittest.mock import MagicMock, patch

from todo_agent.api.services.ai_service import generate_response


@patch("todo_agent.api.services.ai_service.llm_client")
def test_generate_response(mock_client):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Hello from Gemini!"

    mock_client.chat.completions.create.return_value = mock_response

    result = generate_response("Say hello.")

    assert result == "Hello from Gemini!"

    mock_client.chat.completions.create.assert_called_once()
