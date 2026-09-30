def test_create_and_list_items(client):
    r = client.post("/api/v1/items", json={"product_id": "A1", "name": "Widget", "fabric_type": "Cotton", "price_inr": "125.50"})
    assert r.status_code == 201
    item = client.get("/api/v1/items").json()[0]
    assert item["product_id"] == "A1"
    assert item["name"] == "Widget"
    assert item["fabric_type"] == "Cotton"
    assert item["price_inr"] == "125.50"


def test_duplicate_product_id_conflict(client):
    client.post("/api/v1/items", json={"product_id": "A1", "name": "Widget", "fabric_type": "Cotton", "price_inr": "125.50"})
    r = client.post("/api/v1/items", json={"product_id": "A1", "name": "Other", "fabric_type": "Linen", "price_inr": "99.00"})
    assert r.status_code == 409


def test_update_and_delete_item(client):
    item = client.post("/api/v1/items", json={"product_id": "A1", "name": "Widget", "fabric_type": "Cotton", "price_inr": "125.50"}).json()
    r = client.patch(f"/api/v1/items/{item['id']}", json={"name": "Widget 2", "fabric_type": "Linen", "price_inr": "99.95"})
    assert r.json()["name"] == "Widget 2"
    assert r.json()["fabric_type"] == "Linen"
    assert r.json()["price_inr"] == "99.95"
    assert client.delete(f"/api/v1/items/{item['id']}").status_code == 204
    assert client.get(f"/api/v1/items/{item['id']}").status_code == 404


def test_cannot_delete_item_with_movements(client, seed):
    client.post("/api/v1/stock-in", json={"item_id": seed["item"]["id"], "warehouse_id": seed["warehouse"]["id"], "quantity": 5})
    assert client.delete(f"/api/v1/items/{seed['item']['id']}").status_code == 409


def test_price_must_be_non_negative(client):
    response = client.post(
        "/api/v1/items",
        json={"product_id": "A1", "name": "Widget", "fabric_type": "Cotton", "price_inr": "-0.01"},
    )
    assert response.status_code == 422
