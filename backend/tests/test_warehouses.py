def test_create_and_list_warehouses(client):
    r = client.post("/api/v1/warehouses", json={"code": "W1", "name": "North", "location": "Tiruppur"})
    assert r.status_code == 201
    assert len(client.get("/api/v1/warehouses").json()) == 1


def test_duplicate_code_conflict(client):
    client.post("/api/v1/warehouses", json={"code": "W1", "name": "North"})
    assert client.post("/api/v1/warehouses", json={"code": "W1", "name": "South"}).status_code == 409


def test_update_and_delete_warehouse(client):
    wh = client.post("/api/v1/warehouses", json={"code": "W1", "name": "North"}).json()
    assert client.patch(f"/api/v1/warehouses/{wh['id']}", json={"name": "N2"}).json()["name"] == "N2"
    assert client.delete(f"/api/v1/warehouses/{wh['id']}").status_code == 204
