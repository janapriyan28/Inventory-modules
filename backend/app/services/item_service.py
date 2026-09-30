from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.item import Item
from app.repositories.item_repository import ItemRepository
from app.repositories.stock_in_repository import StockInRepository
from app.repositories.stock_out_repository import StockOutRepository
from app.schemas.item import ItemCreate, ItemUpdate


class ItemService:
    def __init__(self, db: Session):
        self.repo = ItemRepository(db)
        self.stock_in = StockInRepository(db)
        self.stock_out = StockOutRepository(db)

    def list(self) -> list[Item]:
        return self.repo.list()

    def get(self, item_id: int) -> Item:
        item = self.repo.get(item_id)
        if not item:
            raise NotFoundError(f"Item {item_id} not found")
        return item

    def create(self, data: ItemCreate) -> Item:
        if self.repo.get_by_product_id(data.product_id):
            raise ConflictError(f"Product ID '{data.product_id}' already exists")
        return self.repo.add(Item(**data.model_dump()))

    def update(self, item_id: int, data: ItemUpdate) -> Item:
        item = self.get(item_id)
        changes = data.model_dump(exclude_unset=True)
        new_product_id = changes.get("product_id")
        if new_product_id and new_product_id != item.product_id and self.repo.get_by_product_id(new_product_id):
            raise ConflictError(f"Product ID '{new_product_id}' already exists")
        for key, value in changes.items():
            setattr(item, key, value)
        return self.repo.save(item)

    def delete(self, item_id: int) -> None:
        item = self.get(item_id)
        if self.stock_in.count_for_item(item_id) or self.stock_out.count_for_item(item_id):
            raise ConflictError("Item has stock movements; deactivate it instead of deleting")
        self.repo.delete(item)
