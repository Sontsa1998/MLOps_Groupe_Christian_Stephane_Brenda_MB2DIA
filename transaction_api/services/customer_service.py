"""Customer service for business logic."""

from transaction_api.logging_config import get_logger
from transaction_api.repository import TransactionRepository

logger = get_logger(__name__)


class CustomerService:
    """Service for customer operations."""

    def __init__(self, repository: TransactionRepository) -> None:
        """Initialize the service."""
        self.repository = repository
