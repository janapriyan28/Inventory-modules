import csv
import io

from app.schemas.current_stock import CurrentStockRow

HEADERS = ["Product ID", "Product Name", "Unit", "Warehouse", "Quantity", "Reorder Level", "Low Stock"]


def current_stock_to_csv(rows: list[CurrentStockRow]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(HEADERS)
    for r in rows:
        writer.writerow(
            [r.product_id, r.item_name, r.unit, r.warehouse_name, r.quantity, r.reorder_level, "YES" if r.is_low else "NO"]
        )
    return buf.getvalue()
