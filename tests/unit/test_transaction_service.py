"""Unit tests for TransactionService."""

import pytest

from transaction_api.exceptions import TransactionNotFound
from transaction_api.services.transaction_service import TransactionService


@pytest.fixture
def service(repository_with_data):
    """Create a transaction service with sample data."""
    return TransactionService(repository_with_data)