from fastapi import APIRouter

from app.api import current_stock, items, stock_in, stock_out, warehouses

api_router = APIRouter()
api_router.include_router(items.router)
api_router.include_router(warehouses.router)
api_router.include_router(stock_in.router)
api_router.include_router(stock_out.router)
api_router.include_router(current_stock.router)
