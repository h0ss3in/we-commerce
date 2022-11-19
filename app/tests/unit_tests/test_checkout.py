from app.dependencies import CheckoutHandler


def test_initial_checkout():
    checkout = CheckoutHandler(items=["001", "002", "001", "004", "003"])
    assert checkout.item_ids == ["001", "002", "001", "004", "003"]
    assert checkout.checkout_lines == {}
    assert checkout.total_price == 0


def test_create_checkout_lines():
    checkout = CheckoutHandler(items=["001", "002", "001", "004", "003"])
    checkout.create_checkout_lines()
    assert checkout.checkout_lines == {
        "001": {
            "name": "Rolex",
            "amount": 2,
            "unit_price": 100,
            "discount": {
                "amount_required": 3,
                "discounted_price": 200
            }
        },
        "002": {
            "name": "Michael Kors",
            "amount": 1,
            "unit_price": 80,
            "discount": {
                "amount_required": 2,
                "discounted_price": 120
            }
        },
        "003": {
            "name": "Swatch",
            "amount": 1,
            "unit_price": 50
        },
        "004": {
            "name": "Casio",
            "amount": 1,
            "unit_price": 30
        },
    }


def test_init_checkout_line():
    checkout = CheckoutHandler(items=["001", "002", "001", "004", "003"])
    checkout.init_checkout_line("001")
    assert checkout.checkout_lines["001"] == {
        "name": "Rolex",
        "amount": 0,
        "unit_price": 100,
        "discount": {
            "amount_required": 3,
            "discounted_price": 200
        }
    }


def test_calculate_total_price():
    checkout = CheckoutHandler(items=["001", "002", "001", "004", "003"])
    checkout.create_checkout_lines()
    checkout.calculate_total_price()
    assert checkout.total_price == 360


def test_calculate_checkout_line_price():
    checkout = CheckoutHandler(items=["001", "001", "001", "004", "003", "003"])
    checkout.create_checkout_lines()
    assert checkout.calculate_checkout_line_price(checkout.checkout_lines["001"]) == 200
    assert checkout.calculate_checkout_line_price(checkout.checkout_lines["003"]) == 100
