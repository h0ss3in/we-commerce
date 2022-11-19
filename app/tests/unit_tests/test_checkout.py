from app.dependencies import CheckoutHandler


def test_initial_checkout():
    checkout = CheckoutHandler(items=["001", "002", "001", "004", "003"])
    assert checkout.item_ids == ["001", "002", "001", "004", "003"]
    assert checkout.checkout_lines == {}
    assert checkout.total_price == 0


def test_create_checkout():
    checkout = CheckoutHandler(items=["001", "002", "001", "004", "003"])
    checkout.create_checkout_lines()
    assert checkout.checkout_lines == {
        "001": {
            "amount": 2,
            "unit_price": 100,
            "discount": {
                "amount_required": 3,
                "discounted_price": 200
            }
        },
        "002": {
            "amount": 1,
            "unit_price": 80,
            "discount": {
                "amount_required": 2,
                "discounted_price": 120
            }
        },
        "003": {
            "amount": 1,
            "unit_price": 50
        },
        "004": {
            "amount": 1,
            "unit_price": 30
        },
    }
