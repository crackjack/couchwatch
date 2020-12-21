import os
from fastapi.testclient import TestClient

from main import app
from tests import override_get_db, test_sqlite_engine

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
    response = client.get("/browse/82739")
    assert response.status_code == 404

    post_data = {"netflix_id": "1234", "name": "fake"}
    client.post("/browse/", json=post_data)
    response = client.get("/browse/1234")
    assert response.status_code == 200


def test_create_entry():
    post_data = {"netflix_id": "1234", "name": "fake"}
    response = client.post("/browse/", json=post_data)
    assert response.status_code == 201
    assert response.json()["name"] == "fake"
    assert response.json()["netflix_id"] == "1234"


def test_delete_entry():
    post_data = {"netflix_id": "1234", "name": "fake"}
    client.post("/browse/", json=post_data)

    response = client.delete("/browse/4321")
    assert response.status_code == 404

    response = client.delete("/browse/1234")
    assert response.status_code == 200
