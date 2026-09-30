from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.current_stock import CurrentStockRow
from app.services.stock_service import StockService
from app.utils.csv_export import current_stock_to_csv

router = APIRouter(prefix="/stock", tags=["Current Stock"])


@router.get("/current", response_model=list[CurrentStockRow])
def current_stock(warehouse_id: int | None = None, low_only: bool = False, db: Session = Depends(get_db)):
    return StockService(db).current_stock(warehouse_id, low_only)


@router.get("/low", response_model=list[CurrentStockRow])
def low_stock(warehouse_id: int | None = None, db: Session = Depends(get_db)):
    return StockService(db).current_stock(warehouse_id, low_only=True)


@router.get("/current/export")
def export_current_stock(warehouse_id: int | None = None, low_only: bool = False, db: Session = Depends(get_db)):
    rows = StockService(db).current_stock(warehouse_id, low_only)
    return Response(
        content=current_stock_to_csv(rows),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="current_stock.csv"'},
    )
