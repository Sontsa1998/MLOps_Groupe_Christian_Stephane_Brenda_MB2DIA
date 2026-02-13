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


def test_get_transaction_by_id_not_found(service):
    """Test getting a non-existent transaction."""
    with pytest.raises(TransactionNotFound):
        service.get_transaction_by_id("nonexistent")


def test_delete_transaction_existing(service):
    """Test deleting an existing transaction."""
    service.delete_transaction("1")
    with pytest.raises(TransactionNotFound):
        service.get_transaction_by_id("1")