from pydantic import BaseModel


class CurrentStockRow(BaseModel):
    item_id: int
    product_id: str
    item_name: str
    unit: str
    warehouse_id: int
    warehouse_name: str
    quantity: int
    reorder_level: int
    is_low: bool
