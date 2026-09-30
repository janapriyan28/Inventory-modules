from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.item import Item


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> list[Item]:
        return list(self.db.scalars(select(Item).order_by(Item.name)))

    def get(self, item_id: int) -> Item | None:
        return self.db.get(Item, item_id)

    def get_by_product_id(self, product_id: str) -> Item | None:
        return self.db.scalar(select(Item).where(Item.product_id == product_id))

    def add(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def save(self, item: Item) -> Item:
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item: Item) -> None:
        self.db.delete(item)
        self.db.commit()
