# Database schema

| Table | Columns |
|---|---|
| `items` | id, product_id (unique), name, fabric_type, unit, reorder_level, is_active, created_at |
| `warehouses` | id, code (unique), name, location, is_active, created_at |
| `stock_in` | id, item_id → items, warehouse_id → warehouses, quantity (>0), reference, remarks, created_at |
| `stock_out` | id, item_id → items, warehouse_id → warehouses, quantity (>0), reference, remarks, created_at |

Indexes: `items.product_id`, `warehouses.code`, and `item_id` / `warehouse_id` on both movement tables.
