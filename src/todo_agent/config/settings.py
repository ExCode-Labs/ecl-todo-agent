from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Server configuration
    app_name: str = "todo-agent"
    app_version: str = "1.0.0"
    port: int = 8001

    # AI configuration
    ai_provider: str = "gemini"

    # Gemini configuration
    gemini_api_key: str = ""
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
    gemini_model: str = "gemini-3.6-flash"

    # Load values from .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
