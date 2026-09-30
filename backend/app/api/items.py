from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("", response_model=list[ItemRead])
def list_items(db: Session = Depends(get_db)):
    return ItemService(db).list()


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemCreate, db: Session = Depends(get_db)):
    return ItemService(db).create(data)


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService(db).get(item_id)


@router.patch("/{item_id}", response_model=ItemRead)
def update_item(item_id: int, data: ItemUpdate, db: Session = Depends(get_db)):
    return ItemService(db).update(item_id, data)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    ItemService(db).delete(item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
