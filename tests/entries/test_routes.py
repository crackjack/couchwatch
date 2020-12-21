import os
from fastapi.testclient import TestClient

from main import app
from tests import override_get_db, test_sqlite_engine

from db import get_db, Base


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

Base.metadata.create_all(bind=test_sqlite_engine)

fake_data = {
  "show_id": "1111",
  "title": "Fake",
  "type": "TV Show",
  "directors": [
    {
      "name": "Director2"
    }
  ],
  "casts": [
    {
      "name": "Actor1"
    }
  ],
  "countries": [
    {
      "name": "United States"
    },
    {
      "name": "Canada"
    }
  ],
  "date_added": "2020-12-20",
  "release_year": "2020",
  "rating": "TV-PG",
  "duration": "3 Seasons",
  "listed_in": [
    {
      "name": "Comedy"
    },
    {
      "name": "Action"
    }
  ]
}


def test_get_entries():
    response = client.get("/browse/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_entry():
    response = client.get("/browse/82739")
    assert response.status_code == 404

    client.post("/browse/", json=fake_data)
    response = client.get("/browse/1111")
    assert response.status_code == 200


def test_create_entry():
    response = client.post("/browse/", json=fake_data)
    assert response.status_code == 409

    fake_data['title'] = "Another Fake"
    fake_data['show_id'] = "1234"
    response = client.post("/browse/", json=fake_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Another Fake"
    assert response.json()["show_id"] == "1234"


def test_delete_entry():
    response = client.delete("/browse/4321")
    assert response.status_code == 404

    response = client.delete("/browse/1111")
    assert response.status_code == 200
