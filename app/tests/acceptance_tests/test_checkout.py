from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_checkout_price_without_discount():
    response = client.post(
        "/checkout/",
        json=[
            "001",
            "002",
            "001",
            "004",
            "003"
        ]
    )
    assert response.status_code == 200
    assert response.json() == {
        "price": 360
    }


def test_checkout_price_with_discount():
    response = client.post(
        "/checkout/",
        json=[
            "001",
            "002",
            "001",
            "004",
            "001",
            "003",
            "001",
            "002",
            "001",
            "003",
            "001",
            "004",
            "001",
        ]
    )
    assert response.status_code == 200
    assert response.json() == {
        "price": 780
    }


def test_checkout_no_items():
    response = client.post(
        "/checkout/",
        json=[]
    )
    assert response.status_code == 200
    assert response.json() == {
        "price": 0
    }


def test_checkout_single_item():
    response = client.post(
        "/checkout/",
        json=[
            "001"
        ]
    )
    assert response.status_code == 200
    assert response.json() == {
        "price": 100
    }


def test_checkout_not_existing_item():
    response = client.post(
        "/checkout/",
        json=[
            "005"
        ]
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Item 005 does not exist!"
    }
