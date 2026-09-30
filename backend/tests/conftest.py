import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import get_db
from app.main import app
from app.models import Base


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    TestingSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture()
def seed(client):
    item = client.post("/api/v1/items", json={"product_id": "BOLT-10", "name": "Bolt M10", "fabric_type": "Steel", "price_inr": "425.50", "reorder_level": 10}).json()
    wh = client.post("/api/v1/warehouses", json={"code": "WH1", "name": "Main Warehouse"}).json()
    return {"item": item, "warehouse": wh}
