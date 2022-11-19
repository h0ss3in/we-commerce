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
