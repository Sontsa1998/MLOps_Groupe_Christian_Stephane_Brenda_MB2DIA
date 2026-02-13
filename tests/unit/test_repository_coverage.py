"""Unit tests to improve repository coverage."""

import pytest
from transaction_api.repository import TransactionRepository


@pytest.fixture(scope="module")
def repository():
    """Create repository with test data."""
    repo = TransactionRepository()
    repo.load_from_csv("./data/transactions.csv")
    return repo

class TestRepositoryExtended:
    """Extended tests for repository."""

    def test_get_all_transactions(self, repository):
        """Test getting all transactions."""
        transactions = repository.get_all_transactions()
        assert len(transactions) > 0
    
    def test_get_by_id(self, repository):
        """Test getting transaction by ID."""
        transactions = repository.get_all_transactions()
        if transactions:
            transaction_id = transactions[0].id
            result = repository.get_by_id(transaction_id)
            assert result is not None
            assert result.id == transaction_id

    def test_get_by_customer(self, repository):
        """Test getting transactions by customer."""
        result, total = repository.get_by_customer("1556")
        assert isinstance(result, list)
        assert isinstance(total, int)
    
    def test_get_by_merchant(self, repository):
        """Test getting transactions by merchant."""
        result, total = repository.get_by_merchant("1556")
        assert isinstance(result, list)
        assert isinstance(total, int)