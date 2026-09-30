from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.stock_out import StockOut


class StockOutRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, item_id: int | None = None, warehouse_id: int | None = None) -> list[StockOut]:
        stmt = select(StockOut).order_by(StockOut.created_at.desc(), StockOut.id.desc())
        if item_id:
            stmt = stmt.where(StockOut.item_id == item_id)
        if warehouse_id:
            stmt = stmt.where(StockOut.warehouse_id == warehouse_id)
        return list(self.db.scalars(stmt).unique())

    def add(self, entry: StockOut) -> StockOut:
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def total(self, item_id: int, warehouse_id: int) -> int:
        stmt = select(func.coalesce(func.sum(StockOut.quantity), 0)).where(
            StockOut.item_id == item_id, StockOut.warehouse_id == warehouse_id
        )
        return int(self.db.scalar(stmt) or 0)

    def totals_by_item_warehouse(self) -> dict[tuple[int, int], int]:
        stmt = select(StockOut.item_id, StockOut.warehouse_id, func.sum(StockOut.quantity)).group_by(
            StockOut.item_id, StockOut.warehouse_id
        )
        return {(i, w): int(q) for i, w, q in self.db.execute(stmt)}

    def count_for_item(self, item_id: int) -> int:
        return int(self.db.scalar(select(func.count()).select_from(StockOut).where(StockOut.item_id == item_id)) or 0)

    def count_for_warehouse(self, warehouse_id: int) -> int:
        return int(
            self.db.scalar(select(func.count()).select_from(StockOut).where(StockOut.warehouse_id == warehouse_id)) or 0
        )
