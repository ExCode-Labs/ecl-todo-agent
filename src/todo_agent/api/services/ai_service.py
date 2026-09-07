from openai import OpenAI

from todo_agent.clients.llm_client import create_llm_client
from todo_agent.config.settings import settings

llm_client: OpenAI | None = None


def generate_response(prompt: str) -> str:
    """
    Send the user's prompt to the configured LLM
    and return the generated response.
    """

    client = llm_client
    if client is None:
        client = create_llm_client()

    response = client.chat.completions.create(
        model=settings.gemini_model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content or ""
