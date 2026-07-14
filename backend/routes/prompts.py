"""Prompts API routes."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/prompts", tags=["prompts"])


class PromptRequest(BaseModel):
    """Prompt request model."""
    title: str
    content: str
    version: str = "1.0.0"


@router.get("/")
async def list_prompts():
    """List all prompts."""
    return {"prompts": [], "total": 0}


@router.post("/")
async def create_prompt(prompt: PromptRequest):
    """Create a new prompt."""
    return {"id": "prompt_1", "status": "created", "prompt": prompt}


@router.get("/{prompt_id}")
async def get_prompt(prompt_id: str):
    """Get a specific prompt."""
    return {"id": prompt_id, "status": "found"}
