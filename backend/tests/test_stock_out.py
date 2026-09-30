def _payload(seed, qty):
    return {"item_id": seed["item"]["id"], "warehouse_id": seed["warehouse"]["id"], "quantity": qty}


def test_stock_out_reduces_stock(client, seed):
    client.post("/api/v1/stock-in", json=_payload(seed, 50))
    assert client.post("/api/v1/stock-out", json=_payload(seed, 20)).status_code == 201
    assert client.get("/api/v1/stock/current").json()[0]["quantity"] == 30


def test_stock_out_insufficient_stock(client, seed):
    client.post("/api/v1/stock-in", json=_payload(seed, 5))
    r = client.post("/api/v1/stock-out", json=_payload(seed, 6))
    assert r.status_code == 422
    assert "Insufficient stock" in r.json()["detail"]
