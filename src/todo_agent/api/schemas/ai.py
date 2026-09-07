from pydantic import BaseModel, Field


class AITestRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        description="Prompt to send to the AI model",
    )


class AITestResponse(BaseModel):
    success: bool
    response: str
