from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class WarehouseBase(BaseModel):
    code: str = Field(min_length=1, max_length=30)
    name: str = Field(min_length=1, max_length=200)
    location: str | None = Field(default=None, max_length=300)
    is_active: bool = True


class WarehouseCreate(WarehouseBase):
    pass


class WarehouseUpdate(BaseModel):
    code: str | None = Field(default=None, min_length=1, max_length=30)
    name: str | None = Field(default=None, min_length=1, max_length=200)
    location: str | None = Field(default=None, max_length=300)
    is_active: bool | None = None


class WarehouseRead(WarehouseBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
