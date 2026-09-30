from sqlalchemy.orm import Session

from app.repositories.item_repository import ItemRepository
from app.repositories.stock_in_repository import StockInRepository
from app.repositories.stock_out_repository import StockOutRepository
from app.repositories.warehouse_repository import WarehouseRepository
from app.schemas.current_stock import CurrentStockRow


class StockService:
    """Current stock = total stock-in minus total stock-out, per item and warehouse."""

    def __init__(self, db: Session):
        self.items = ItemRepository(db)
        self.warehouses = WarehouseRepository(db)
        self.stock_in = StockInRepository(db)
        self.stock_out = StockOutRepository(db)

    def current_stock(
        self, warehouse_id: int | None = None, low_only: bool = False
    ) -> list[CurrentStockRow]:
        ins = self.stock_in.totals_by_item_warehouse()
        outs = self.stock_out.totals_by_item_warehouse()
        items = {i.id: i for i in self.items.list()}
        warehouses = {w.id: w for w in self.warehouses.list()}

        rows: list[CurrentStockRow] = []
        for key in set(ins) | set(outs):
            item_id, wh_id = key
            if warehouse_id and wh_id != warehouse_id:
                continue
            item, wh = items.get(item_id), warehouses.get(wh_id)
            if not item or not wh:
                continue
            qty = ins.get(key, 0) - outs.get(key, 0)
            is_low = qty <= item.reorder_level
            if low_only and not is_low:
                continue
            rows.append(
                CurrentStockRow(
                    item_id=item.id, product_id=item.product_id, item_name=item.name, unit=item.unit,
                    warehouse_id=wh.id, warehouse_name=wh.name, quantity=qty,
                    reorder_level=item.reorder_level, is_low=is_low,
                )
            )
        rows.sort(key=lambda r: (r.item_name.lower(), r.warehouse_name.lower()))
        return rows
