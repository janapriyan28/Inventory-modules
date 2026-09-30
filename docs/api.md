# API (base path `/api/v1`, interactive docs at `/docs`)

| Method | Path | Notes |
|---|---|---|
| GET/POST | `/items` | list / create |
| GET/PATCH/DELETE | `/items/{id}` | delete blocked (409) if item has movements |
| GET/POST | `/warehouses` | list / create |
| GET/PATCH/DELETE | `/warehouses/{id}` | delete blocked (409) if warehouse has movements |
| GET/POST | `/stock-in` | filters: `item_id`, `warehouse_id` |
| GET/POST | `/stock-out` | 422 if quantity exceeds available stock |
| GET | `/stock/current` | filters: `warehouse_id`, `low_only` |
| GET | `/stock/low` | rows at or below reorder level |
| GET | `/stock/current/export` | CSV download, same filters as `/stock/current` |

Errors are returned as `{ "detail": "message" }` (404 not found, 409 conflict, 422 rule/validation).

Items use a unique `product_id`, `name` (shown as Product Name), required `fabric_type`, and a non-negative `price_inr` amount with two decimal places; stock responses and exports include Product ID.
