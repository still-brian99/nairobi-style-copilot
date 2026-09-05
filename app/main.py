from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.ai.agent import run_agent

app = FastAPI(title="Nairobi Style Copilot", version="0.1.0")


class CopilotRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=4000)


class CopilotResponse(BaseModel):
    response: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "nairobi-style-copilot"}


@app.post("/api/v1/copilot", response_model=CopilotResponse)
def copilot(request: CopilotRequest) -> CopilotResponse:
    return CopilotResponse(response=run_agent(request.prompt))
