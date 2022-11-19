class CheckoutHandler:

    def __init__(self, items: list[str]):
        self.item_ids = items
        self.checkout_lines = {}
        self.total_price = 0

    def create(self):
        self.create_checkout_lines()
        # TODO: create the checkout
        self.total_price = 360

    def create_checkout_lines(self):
        self.checkout_lines = {
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
