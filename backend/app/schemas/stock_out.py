from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class StockOutCreate(BaseModel):
    item_id: int
    warehouse_id: int
    quantity: int = Field(gt=0)
    reference: str | None = Field(default=None, max_length=100)
    remarks: str | None = Field(default=None, max_length=500)


class StockOutRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    item_id: int
    item_product_id: str
    item_name: str
    warehouse_id: int
    warehouse_name: str
    quantity: int
    reference: str | None
    remarks: str | None
    created_at: datetime
