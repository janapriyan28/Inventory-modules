from sqlalchemy.orm import Session

from app.core.exceptions import BusinessRuleError
from app.models.stock_in import StockIn
from app.repositories.stock_in_repository import StockInRepository
from app.schemas.stock_in import StockInCreate
from app.services.item_service import ItemService
from app.services.warehouse_service import WarehouseService


class StockInService:
    def __init__(self, db: Session):
        self.repo = StockInRepository(db)
        self.items = ItemService(db)
        self.warehouses = WarehouseService(db)

    def list(self, item_id: int | None = None, warehouse_id: int | None = None) -> list[StockIn]:
        return self.repo.list(item_id, warehouse_id)

    def create(self, data: StockInCreate) -> StockIn:
        item = self.items.get(data.item_id)
        warehouse = self.warehouses.get(data.warehouse_id)
        if not item.is_active or not warehouse.is_active:
            raise BusinessRuleError("Item and warehouse must both be active")
        return self.repo.add(StockIn(**data.model_dump()))
