"""Customer API routes."""

from fastapi import APIRouter

from transaction_api.logging_config import get_logger

logger = get_logger(__name__)

router: APIRouter = APIRouter(prefix="/api/customers", tags=["customers"])
