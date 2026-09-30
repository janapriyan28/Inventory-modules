from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.warehouse import WarehouseCreate, WarehouseRead, WarehouseUpdate
from app.services.warehouse_service import WarehouseService

router = APIRouter(prefix="/warehouses", tags=["Warehouses"])


@router.get("", response_model=list[WarehouseRead])
def list_warehouses(db: Session = Depends(get_db)):
    return WarehouseService(db).list()


@router.post("", response_model=WarehouseRead, status_code=status.HTTP_201_CREATED)
def create_warehouse(data: WarehouseCreate, db: Session = Depends(get_db)):
    return WarehouseService(db).create(data)


@router.get("/{warehouse_id}", response_model=WarehouseRead)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return WarehouseService(db).get(warehouse_id)


@router.patch("/{warehouse_id}", response_model=WarehouseRead)
def update_warehouse(warehouse_id: int, data: WarehouseUpdate, db: Session = Depends(get_db)):
    return WarehouseService(db).update(warehouse_id, data)


@router.delete("/{warehouse_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    WarehouseService(db).delete(warehouse_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
