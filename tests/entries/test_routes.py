from fastapi.testclient import TestClient

from main import app
from tests import override_get_db, test_sqlite_engine, TestingSessionLocal

from entries.routes import get_db
from entries.models import Base


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

Base.metadata.create_all(bind=test_sqlite_engine)


def test_get_entries():
    response = client.get("/browse/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_entry():
    response = client.get("/browse/12345")
    assert response.status_code == 404
    assert response.json() == {"detail": "Entry not Found"}
    Base.metadata.create_all(test_sqlite_engine)


def test_create_entry():
    post_data = {"netflix_id": 1234, "name": "fake"}
    response = client.post("/browse/", json=post_data)
    assert response.status_code == 201
    assert response.json()["name"] == "fake"
    assert "netflix_id" not in response.json().keys()
    Base.metadata.create_all(test_sqlite_engine)
