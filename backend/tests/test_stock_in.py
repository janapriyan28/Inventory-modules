def test_stock_in_creates_entry(client, seed):
    r = client.post(
        "/api/v1/stock-in",
        json={"item_id": seed["item"]["id"], "warehouse_id": seed["warehouse"]["id"], "quantity": 50, "reference": "PO-1"},
    )
    assert r.status_code == 201
    assert r.json()["item_name"] == "Bolt M10"
    assert len(client.get("/api/v1/stock-in").json()) == 1


def test_stock_in_rejects_non_positive_quantity(client, seed):
    r = client.post("/api/v1/stock-in", json={"item_id": seed["item"]["id"], "warehouse_id": seed["warehouse"]["id"], "quantity": 0})
    assert r.status_code == 422


def test_stock_in_unknown_item(client, seed):
    r = client.post("/api/v1/stock-in", json={"item_id": 999, "warehouse_id": seed["warehouse"]["id"], "quantity": 1})
    assert r.status_code == 404
