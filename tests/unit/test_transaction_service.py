"""Unit tests for TransactionService."""

import pytest

from transaction_api.exceptions import TransactionNotFound
from transaction_api.services.transaction_service import TransactionService


@pytest.fixture
def service(repository_with_data):
    """Create a transaction service with sample data."""
    return TransactionService(repository_with_data)


def test_get_transaction_by_id_existing(service, sample_transactions):
    """Test getting an existing transaction by ID."""
    transaction = service.get_transaction_by_id("1")
    assert transaction.id == "1"
    assert transaction.client_id == "C001"
    assert transaction.amount == 100.0