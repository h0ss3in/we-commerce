from app.database import database


class CheckoutHandler:

    def __init__(self, items: list[str]):
        self.item_ids = items
        self.checkout_lines = {}
        self.total_price = 0
        self.db = database

    def create(self):
        self.create_checkout_lines()
        self.calculate_total_price()

    def create_checkout_lines(self):
        for item_id in self.item_ids:
            if item_id not in self.checkout_lines:
                self.init_checkout_line(item_id)
            self.checkout_lines[item_id]["amount"] += 1

    def calculate_total_price(self):
        self.total_price = 360

    def init_checkout_line(self, item_id):
        self.checkout_lines[item_id] = {
            **self.db["products"][item_id],
            "amount": 0
        }

    @classmethod
    def calculate_discounted_price(cls, checkout_line):
        return 200
