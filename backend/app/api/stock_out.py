from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.stock_out import StockOutCreate, StockOutRead
from app.services.stock_out_service import StockOutService

router = APIRouter(prefix="/stock-out", tags=["Stock Out"])


@router.get("", response_model=list[StockOutRead])
def list_entries(item_id: int | None = None, warehouse_id: int | None = None, db: Session = Depends(get_db)):
    return StockOutService(db).list(item_id, warehouse_id)


@router.post("", response_model=StockOutRead, status_code=status.HTTP_201_CREATED)
def create_entry(data: StockOutCreate, db: Session = Depends(get_db)):
    return StockOutService(db).create(data)
