from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.stock_in import StockInCreate, StockInRead
from app.services.stock_in_service import StockInService

router = APIRouter(prefix="/stock-in", tags=["Stock In"])


@router.get("", response_model=list[StockInRead])
def list_entries(item_id: int | None = None, warehouse_id: int | None = None, db: Session = Depends(get_db)):
    return StockInService(db).list(item_id, warehouse_id)


@router.post("", response_model=StockInRead, status_code=status.HTTP_201_CREATED)
def create_entry(data: StockInCreate, db: Session = Depends(get_db)):
    return StockInService(db).create(data)
