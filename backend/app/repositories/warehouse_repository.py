from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.warehouse import Warehouse


class WarehouseRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> list[Warehouse]:
        return list(self.db.scalars(select(Warehouse).order_by(Warehouse.name)))

    def get(self, warehouse_id: int) -> Warehouse | None:
        return self.db.get(Warehouse, warehouse_id)

    def get_by_code(self, code: str) -> Warehouse | None:
        return self.db.scalar(select(Warehouse).where(Warehouse.code == code))

    def add(self, warehouse: Warehouse) -> Warehouse:
        self.db.add(warehouse)
        self.db.commit()
        self.db.refresh(warehouse)
        return warehouse

    def save(self, warehouse: Warehouse) -> Warehouse:
        self.db.commit()
        self.db.refresh(warehouse)
        return warehouse

    def delete(self, warehouse: Warehouse) -> None:
        self.db.delete(warehouse)
        self.db.commit()
