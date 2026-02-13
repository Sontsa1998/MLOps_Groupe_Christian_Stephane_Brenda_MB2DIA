"""Pydantic models for the Transaction API."""

from datetime import date as date_type
from datetime import datetime
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class Transaction(BaseModel):
    """Transaction data model."""

    id: str = Field(..., description="Transaction id")
    date: datetime = Field(..., description="Transaction date and time")
    client_id: str = Field(..., description="Client id")
    card_id: str = Field(..., description="Card id")
    amount: float = Field(..., description="Amount")
    use_chip: str = Field(..., description="Transaction type")
    merchant_id: str = Field(..., description="Merchant id")
    merchant_city: str = Field(..., description="Merchant city")
    merchant_state: str = Field(..., description="Merchant state")
    zip: str = Field(..., description="ZIP code")
    mcc: str = Field(..., description="Merchant category code")
    errors: Optional[str] = Field(None, description="Error flag")