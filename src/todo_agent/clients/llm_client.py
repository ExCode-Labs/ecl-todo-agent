from openai import OpenAI

from todo_agent.config.settings import settings


def create_llm_client() -> OpenAI:
    """
    Create an OpenAI client configured to communicate
    with the Gemini OpenAI-compatible API.
    """

    return OpenAI(
        api_key=settings.gemini_api_key,
        base_url=settings.gemini_base_url,
    )
