from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin
from app.models.item import Item
from app.models.warehouse import Warehouse


class StockOut(Base, TimestampMixin):
    __tablename__ = "stock_out"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), index=True)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouses.id"), index=True)
    quantity: Mapped[int] = mapped_column(Integer)
    reference: Mapped[str | None] = mapped_column(String(100), nullable=True)
    remarks: Mapped[str | None] = mapped_column(String(500), nullable=True)

    item: Mapped[Item] = relationship(lazy="joined")
    warehouse: Mapped[Warehouse] = relationship(lazy="joined")

    @property
    def item_product_id(self) -> str:
        return self.item.product_id

    @property
    def item_name(self) -> str:
        return self.item.name

    @property
    def warehouse_name(self) -> str:
        return self.warehouse.name
