from sqlalchemy.orm import Session

from app.core.exceptions import BusinessRuleError
from app.models.stock_out import StockOut
from app.repositories.stock_in_repository import StockInRepository
from app.repositories.stock_out_repository import StockOutRepository
from app.schemas.stock_out import StockOutCreate
from app.services.item_service import ItemService
from app.services.warehouse_service import WarehouseService


class StockOutService:
    def __init__(self, db: Session):
        self.repo = StockOutRepository(db)
        self.stock_in = StockInRepository(db)
        self.items = ItemService(db)
        self.warehouses = WarehouseService(db)

    def list(self, item_id: int | None = None, warehouse_id: int | None = None) -> list[StockOut]:
        return self.repo.list(item_id, warehouse_id)

    def create(self, data: StockOutCreate) -> StockOut:
        item = self.items.get(data.item_id)
        warehouse = self.warehouses.get(data.warehouse_id)
        if not item.is_active or not warehouse.is_active:
            raise BusinessRuleError("Item and warehouse must both be active")
        available = self.stock_in.total(data.item_id, data.warehouse_id) - self.repo.total(
            data.item_id, data.warehouse_id
        )
        if data.quantity > available:
            raise BusinessRuleError(
                f"Insufficient stock: requested {data.quantity}, available {available}"
            )
        return self.repo.add(StockOut(**data.model_dump()))
