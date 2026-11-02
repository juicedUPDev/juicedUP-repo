"""V1 API routes for Maypo platform with RESTful design."""
from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

try:
    from backend.config import FirestoreService
except ImportError:
    from config import FirestoreService

v1_router = APIRouter(prefix="/api/v1", tags=["v1"])


class ConsultationRequest(BaseModel):
    """Request payload for creating a consultation."""

    query: str = Field(..., min_length=1, description="Consultation query")
    topic: str = Field("general", description="Topic of consultation")
    context: str = Field("", description="Additional context")


class SubmitRequest(BaseModel):
    """Request payload for submitting data."""

    data: Dict[str, Any] = Field(..., description="Data to submit")
    type: Optional[str] = Field("general", description="Type of submission")


class PaginationResponse(BaseModel):
    """Pagination metadata returned by list endpoints."""

    skip: int
    limit: int
    total: int


class ConsultationResponse(BaseModel):
    """Response model for consultations."""

    id: str
    topic: str
    query: str
    recommendation: str
    model: str
    confidence: float
    status: str = "completed"
    created_at: str


class ConsultationListResponse(BaseModel):
    """Response payload for listing consultations."""

    data: List[ConsultationResponse]
    pagination: PaginationResponse


class SubmissionResponse(BaseModel):
    """Response model for submissions."""

    id: str
    status: str
    type: str
    data_keys: List[str]
    message: str
    created_at: str
    result: Optional[str] = None
    completed_at: Optional[str] = None


class PromptResponse(BaseModel):
    """Response model for prompt objects."""

    id: str
    name: str
    version: str
    description: Optional[str] = None
    content: Optional[str] = None
    created_at: Optional[str] = None


class PromptListResponse(BaseModel):
    """Response payload for listing prompts."""

    prompts: List[PromptResponse]
    total: int


class UsageAnalyticsResponse(BaseModel):
    """Response model for usage analytics."""

    period: str
    total_requests: int
    total_tokens_used: int
    peak_hour: str
    top_models: List[str]
    average_response_time_ms: Optional[int] = None


CONSULTATIONS: Dict[str, Dict[str, Any]] = {
    "c_101": {
        "id": "c_101",
        "topic": "Prompt Engineering",
        "query": "How to optimize LLM prompts?",
        "recommendation": "Leverage modular prompt architecture and cache repeated completions.",
        "model": "gpt-4o",
        "confidence": 0.95,
        "status": "completed",
        "created_at": "2026-08-28T12:00:00Z",
    },
    "c_102": {
        "id": "c_102",
        "topic": "System Architecture",
        "query": "Design patterns for scalable APIs",
        "recommendation": "Use modular services, bounded contexts, and asynchronous communication for scale.",
        "model": "gpt-4o",
        "confidence": 0.95,
        "status": "in_progress",
        "created_at": "2026-08-29T10:30:00Z",
    },
}

SUBMISSIONS: Dict[str, Dict[str, Any]] = {
    "sub_123": {
        "id": "sub_123",
        "status": "completed",
        "type": "general",
        "result": "Processing completed successfully",
        "created_at": "2026-08-29T11:00:00Z",
        "completed_at": "2026-08-29T11:05:00Z",
    }
}

PROMPTS: Dict[str, Dict[str, Any]] = {
    "p_1": {
        "id": "p_1",
        "name": "System Architecture Expert",
        "version": "1.0.0",
        "description": "Expert advice on system design and architecture",
        "content": "You are an expert in system architecture...",
        "created_at": "2026-01-15T10:00:00Z",
    },
    "p_2": {
        "id": "p_2",
        "name": "Cost Optimization Advisor",
        "version": "1.1.0",
        "description": "Recommendations for reducing infrastructure costs",
        "content": "You are an expert in cost optimization...",
        "created_at": "2026-01-15T10:30:00Z",
    },
}


def _new_consultation_id() -> str:
    return f"c_{uuid4().hex[:8]}"


def _new_submission_id() -> str:
    return f"sub_{uuid4().hex[:8]}"


def _store_consultation(record: Dict[str, Any]) -> Dict[str, Any]:
    try:
        service = FirestoreService("consultations")
        return service.create(record, record["id"])
    except RuntimeError:
        CONSULTATIONS[record["id"]] = record
        return record


def _get_consultation_by_id(consultation_id: str) -> Optional[Dict[str, Any]]:
    try:
        return FirestoreService("consultations").get(consultation_id)
    except RuntimeError:
        return CONSULTATIONS.get(consultation_id)


def _list_consultations(skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    try:
        return FirestoreService("consultations").list(skip=skip, limit=limit)
    except RuntimeError:
        ordered = sorted(CONSULTATIONS.values(), key=lambda item: item["created_at"], reverse=True)
        return ordered[skip : skip + limit]


def _count_consultations() -> int:
    try:
        return FirestoreService("consultations").count()
    except RuntimeError:
        return len(CONSULTATIONS)


def _store_submission(record: Dict[str, Any]) -> Dict[str, Any]:
    try:
        service = FirestoreService("submissions")
        return service.create(record, record["id"])
    except RuntimeError:
        SUBMISSIONS[record["id"]] = record
        return record


def _get_submission_by_id(submission_id: str) -> Optional[Dict[str, Any]]:
    try:
        return FirestoreService("submissions").get(submission_id)
    except RuntimeError:
        return SUBMISSIONS.get(submission_id)


def _store_prompt(record: Dict[str, Any]) -> Dict[str, Any]:
    try:
        service = FirestoreService("prompts")
        return service.create(record, record["id"])
    except RuntimeError:
        PROMPTS[record["id"]] = record
        return record


def _get_prompt_by_id(prompt_id: str) -> Optional[Dict[str, Any]]:
    try:
        return FirestoreService("prompts").get(prompt_id)
    except RuntimeError:
        return PROMPTS.get(prompt_id)


def _list_prompts() -> List[Dict[str, Any]]:
    try:
        return FirestoreService("prompts").list(skip=0, limit=100)
    except RuntimeError:
        return list(PROMPTS.values())


@v1_router.post(
    "/consultations",
    status_code=status.HTTP_201_CREATED,
    response_model=ConsultationResponse,
    summary="Create a new consultation",
    description="Submit a new consultation request with a query and optional topic",
)
async def create_consultation(request: ConsultationRequest):
    """Create a new consultation request."""
    if not request.query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query cannot be empty or whitespace only",
        )

    consultation_id = _new_consultation_id()
    consultation = {
        "id": consultation_id,
        "topic": request.topic,
        "query": request.query,
        "recommendation": f"Consultation result for '{request.query}': Standard prompt optimization applied.",
        "model": "gpt-4o",
        "confidence": 0.95,
        "status": "completed",
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    return _store_consultation(consultation)


@v1_router.get(
    "/consultations/{consultation_id}",
    status_code=status.HTTP_200_OK,
    response_model=ConsultationResponse,
    summary="Retrieve a specific consultation",
    description="Get details of a previously created consultation by ID",
)
async def get_consultation(consultation_id: str):
    """Retrieve a specific consultation."""
    if not consultation_id.startswith("c_"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid consultation ID format. ID must start with 'c_'",
        )

    consultation = _get_consultation_by_id(consultation_id)
    if consultation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Consultation '{consultation_id}' not found",
        )

    return consultation


@v1_router.get(
    "/consultations",
    status_code=status.HTTP_200_OK,
    response_model=ConsultationListResponse,
    summary="List all consultations",
    description="Retrieve consultation history with pagination",
)
async def list_consultations(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum records to return"),
):
    """View consultation history with pagination."""
    consultations = _list_consultations(skip=skip, limit=limit)
    return {
        "data": consultations,
        "pagination": {
            "skip": skip,
            "limit": limit,
            "total": _count_consultations(),
        },
    }


@v1_router.post(
    "/submissions",
    status_code=status.HTTP_201_CREATED,
    response_model=SubmissionResponse,
    summary="Create a new submission",
    description="Submit data for processing",
)
async def create_submission(request: SubmitRequest):
    """Submit data for processing."""
    if not request.data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Submission data cannot be empty",
        )

    submission_id = _new_submission_id()
    submission = {
        "id": submission_id,
        "status": "received",
        "type": request.type or "general",
        "data_keys": list(request.data.keys()),
        "message": "Data successfully queued for processing",
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    return _store_submission(submission)


@v1_router.get(
    "/submissions/{submission_id}",
    status_code=status.HTTP_200_OK,
    response_model=SubmissionResponse,
    summary="Retrieve submission status",
    description="Get the status and details of a submission by ID",
)
async def get_submission(submission_id: str):
    """Retrieve submission details and status."""
    if not submission_id.startswith("sub_"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid submission ID format",
        )

    submission = _get_submission_by_id(submission_id)
    if submission is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Submission '{submission_id}' not found",
        )

    return submission


@v1_router.get(
    "/prompts",
    status_code=status.HTTP_200_OK,
    response_model=PromptListResponse,
    summary="List available prompts",
    description="Retrieve all available prompt templates",
)
async def list_prompts():
    """List all available prompts for consultation."""
    prompts = _list_prompts()
    return {"prompts": prompts, "total": len(prompts)}


@v1_router.get(
    "/prompts/{prompt_id}",
    status_code=status.HTTP_200_OK,
    response_model=PromptResponse,
    summary="Retrieve specific prompt",
    description="Get details of a specific prompt template by ID",
)
async def get_prompt(prompt_id: str):
    """Retrieve details of a specific prompt."""
    if not prompt_id.startswith("p_"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid prompt ID format",
        )

    prompt = _get_prompt_by_id(prompt_id)
    if prompt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prompt '{prompt_id}' not found",
        )

    return prompt


@v1_router.get(
    "/usage-analytics",
    status_code=status.HTTP_200_OK,
    response_model=UsageAnalyticsResponse,
    summary="Get usage statistics",
    description="Retrieve platform usage analytics and metrics",
)
async def get_usage_analytics(
    period: str = Query("7d", description="Analytics period: 7d, 30d, or 90d")
):
    """Get usage statistics and analytics."""
    valid_periods = ["7d", "30d", "90d"]
    if period not in valid_periods:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid period. Must be one of: {', '.join(valid_periods)}",
        )

    return {
        "period": period,
        "total_requests": 1420,
        "total_tokens_used": 284000,
        "peak_hour": "14:00 UTC",
        "top_models": ["gpt-4o", "claude-3-5-sonnet"],
        "average_response_time_ms": 245,
    }


@v1_router.get(
    "/consult",
    include_in_schema=False,
    status_code=status.HTTP_200_OK,
)
async def get_consult_legacy(query: Optional[str] = Query(None, description="Consultation query")):
    """Backward-compatible alias for the original consultation endpoint."""
    return {
        "status": "success",
        "query": query or "General Inquiry",
        "recommendation": "Optimal strategy: Leverage modular prompt architecture and cache repeated LLM completions.",
        "model": "gpt-4o",
        "confidence": 0.95,
    }


@v1_router.post(
    "/consult",
    include_in_schema=False,
    status_code=status.HTTP_201_CREATED,
)
async def post_consult_legacy(request: ConsultationRequest):
    """Backward-compatible alias for the original consultation POST route."""
    return await create_consultation(request)


@v1_router.post(
    "/submit",
    include_in_schema=False,
    status_code=status.HTTP_201_CREATED,
)
async def submit_data_legacy(request: SubmitRequest):
    """Backward-compatible alias for the original submission route."""
    return await create_submission(request)


@v1_router.get(
    "/history",
    include_in_schema=False,
    status_code=status.HTTP_200_OK,
)
async def consultation_history_legacy(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum records to return"),
):
    """Backward-compatible alias for the old consultation history endpoint."""
    return await list_consultations(skip=skip, limit=limit)


@v1_router.get(
    "/analytics/usage",
    include_in_schema=False,
    status_code=status.HTTP_200_OK,
)
async def legacy_usage_analytics(
    period: str = Query("7d", description="Analytics period: 7d, 30d, or 90d")
):
    """Backward-compatible alias for the old usage analytics endpoint."""
    return await get_usage_analytics(period=period)
