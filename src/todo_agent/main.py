from fastapi import FastAPI

from todo_agent.api.routes.ai import router as ai_router
from todo_agent.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


# Register AI routes
app.include_router(
    ai_router,
    prefix="/api/v1",
)


@app.get("/health")
def health_check():
    """
    Basic health check endpoint.
    """

    return {
        "status": "ok",
        "service": settings.app_name,
    }
