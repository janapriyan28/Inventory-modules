# Business rules

1. Product ID and warehouse code must be unique.
2. Stock-in / stock-out quantity must be a positive integer.
3. Stock movements are only allowed for **active** items and warehouses.
4. Stock-out cannot exceed available stock for that item in that warehouse.
5. Current stock = Σ stock-in − Σ stock-out per (item, warehouse).
6. **Low stock**: current quantity ≤ item reorder level.
7. Items and warehouses with movements cannot be deleted – deactivate them instead.
8. Stock movements are append-only (no edit/delete) so history stays auditable.
