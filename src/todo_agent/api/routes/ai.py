from fastapi import APIRouter, HTTPException, Query

from todo_agent.api.schemas.ai import AITestResponse
from todo_agent.api.services.ai_service import generate_response
from todo_agent.core.exceptions import AIServiceError

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.get("/test", response_model=AITestResponse)
def test_ai(
    prompt: str = Query(..., min_length=1),
) -> AITestResponse:
    """
    Test endpoint for verifying LLM connectivity.
    """
    try:
        response = generate_response(prompt)

        return AITestResponse(
            success=True,
            response=response,
        )

    except AIServiceError as error:
        raise HTTPException(
            status_code=500,
            detail=f"AI request failed: {error!s}",
        ) from error
