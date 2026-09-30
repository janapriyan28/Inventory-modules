from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.stock_in import StockIn


class StockInRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, item_id: int | None = None, warehouse_id: int | None = None) -> list[StockIn]:
        stmt = select(StockIn).order_by(StockIn.created_at.desc(), StockIn.id.desc())
        if item_id:
            stmt = stmt.where(StockIn.item_id == item_id)
        if warehouse_id:
            stmt = stmt.where(StockIn.warehouse_id == warehouse_id)
        return list(self.db.scalars(stmt).unique())

    def add(self, entry: StockIn) -> StockIn:
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def total(self, item_id: int, warehouse_id: int) -> int:
        stmt = select(func.coalesce(func.sum(StockIn.quantity), 0)).where(
            StockIn.item_id == item_id, StockIn.warehouse_id == warehouse_id
        )
        return int(self.db.scalar(stmt) or 0)

    def totals_by_item_warehouse(self) -> dict[tuple[int, int], int]:
        stmt = select(StockIn.item_id, StockIn.warehouse_id, func.sum(StockIn.quantity)).group_by(
            StockIn.item_id, StockIn.warehouse_id
        )
        return {(i, w): int(q) for i, w, q in self.db.execute(stmt)}

    def count_for_item(self, item_id: int) -> int:
        return int(self.db.scalar(select(func.count()).select_from(StockIn).where(StockIn.item_id == item_id)) or 0)

    def count_for_warehouse(self, warehouse_id: int) -> int:
        return int(
            self.db.scalar(select(func.count()).select_from(StockIn).where(StockIn.warehouse_id == warehouse_id)) or 0
        )
