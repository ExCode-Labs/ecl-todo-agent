from fastapi import FastAPI

app = FastAPI(
    title="Todo Agent API",
    version="0.1.0",
)


@app.get("/")
async def welcome() -> dict[str, str]:
    return {
        "message": "Welcome to Todo Agent API",
    }
