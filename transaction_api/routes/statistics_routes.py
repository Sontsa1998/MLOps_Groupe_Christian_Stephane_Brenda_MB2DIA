"""Statistics API routes."""

from fastapi import APIRouter, HTTPException, status

from transaction_api import app_context
from transaction_api.logging_config import get_logger
from transaction_api.models import (
    AmountDistribution,
    OverviewStats,
    TypeStats,
)
from transaction_api.services.statistics_service import StatisticsService

logger = get_logger(__name__)

router: APIRouter = APIRouter(prefix="/api/stats", tags=["statistics"])

def get_service() -> StatisticsService:
    """Get statistics service instance."""
    if app_context.repository is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Repository not initialized",
        )
    return StatisticsService(app_context.repository)
