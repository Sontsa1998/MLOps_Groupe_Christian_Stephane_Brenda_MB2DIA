"""Unit tests to improve repository coverage."""

import pytest
from transaction_api.repository import TransactionRepository


@pytest.fixture(scope="module")
def repository():
    """Create repository with test data."""
    repo = TransactionRepository()
    repo.load_from_csv("./data/transactions.csv")
    return repo