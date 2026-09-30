from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ItemBase(BaseModel):
    product_id: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=200)
    fabric_type: str = Field(min_length=1, max_length=100)
    price_inr: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    unit: str = Field(default="pcs", max_length=20)
    reorder_level: int = Field(default=0, ge=0)
    is_active: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    product_id: str | None = Field(default=None, min_length=1, max_length=50)
    name: str | None = Field(default=None, min_length=1, max_length=200)
    fabric_type: str | None = Field(default=None, min_length=1, max_length=100)
    price_inr: Decimal | None = Field(default=None, ge=0, max_digits=12, decimal_places=2)
    unit: str | None = Field(default=None, max_length=20)
    reorder_level: int | None = Field(default=None, ge=0)
    is_active: bool | None = None


class ItemRead(ItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
