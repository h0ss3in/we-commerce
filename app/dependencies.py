from app.database import database


class CheckoutHandler:

    def __init__(self, items: list[str]):
        self.item_ids = items
        self.checkout_lines = {}
        self.total_price = 0
        self.db = database

    def create(self):
        self.create_checkout_lines()
        # TODO: create the checkout
        self.total_price = 360

    def create_checkout_lines(self):
        for item_id in self.item_ids:
            if item_id not in self.checkout_lines:
                self.checkout_lines[item_id] = {
                    **self.db["products"][item_id],
                    "amount": 0
                }
            self.checkout_lines[item_id]["amount"] += 1
