def _move(client, path, seed, qty):
    return client.post(
        f"/api/v1/{path}",
        json={"item_id": seed["item"]["id"], "warehouse_id": seed["warehouse"]["id"], "quantity": qty},
    )


def test_current_stock_and_low_flag(client, seed):
    _move(client, "stock-in", seed, 30)
    row = client.get("/api/v1/stock/current").json()[0]
    assert row["quantity"] == 30 and row["is_low"] is False
    _move(client, "stock-out", seed, 25)
    row = client.get("/api/v1/stock/current").json()[0]
    assert row["quantity"] == 5 and row["is_low"] is True
    assert len(client.get("/api/v1/stock/low").json()) == 1


def test_low_only_filter_excludes_healthy_stock(client, seed):
    _move(client, "stock-in", seed, 100)
    assert client.get("/api/v1/stock/current?low_only=true").json() == []


def test_csv_export(client, seed):
    _move(client, "stock-in", seed, 8)
    r = client.get("/api/v1/stock/current/export")
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("text/csv")
    lines = r.text.strip().splitlines()
    assert lines[0].startswith("Product ID,Product Name")
    assert "BOLT-10" in lines[1] and lines[1].endswith("YES")
