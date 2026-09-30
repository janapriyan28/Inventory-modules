from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.warehouse import Warehouse
from app.repositories.stock_in_repository import StockInRepository
from app.repositories.stock_out_repository import StockOutRepository
from app.repositories.warehouse_repository import WarehouseRepository
from app.schemas.warehouse import WarehouseCreate, WarehouseUpdate


class WarehouseService:
    def __init__(self, db: Session):
        self.repo = WarehouseRepository(db)
        self.stock_in = StockInRepository(db)
        self.stock_out = StockOutRepository(db)

    def list(self) -> list[Warehouse]:
        return self.repo.list()

    def get(self, warehouse_id: int) -> Warehouse:
        wh = self.repo.get(warehouse_id)
        if not wh:
            raise NotFoundError(f"Warehouse {warehouse_id} not found")
        return wh

    def create(self, data: WarehouseCreate) -> Warehouse:
        if self.repo.get_by_code(data.code):
            raise ConflictError(f"Warehouse code '{data.code}' already exists")
        return self.repo.add(Warehouse(**data.model_dump()))

    def update(self, warehouse_id: int, data: WarehouseUpdate) -> Warehouse:
        wh = self.get(warehouse_id)
        changes = data.model_dump(exclude_unset=True)
        new_code = changes.get("code")
        if new_code and new_code != wh.code and self.repo.get_by_code(new_code):
            raise ConflictError(f"Warehouse code '{new_code}' already exists")
        for key, value in changes.items():
            setattr(wh, key, value)
        return self.repo.save(wh)

    def delete(self, warehouse_id: int) -> None:
        wh = self.get(warehouse_id)
        if self.stock_in.count_for_warehouse(warehouse_id) or self.stock_out.count_for_warehouse(warehouse_id):
            raise ConflictError("Warehouse has stock movements; deactivate it instead of deleting")
        self.repo.delete(wh)
