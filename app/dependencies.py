from fastapi import HTTPException

from app.constants.errors import Errors
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
        total_price = 0
        for checkout_line in self.checkout_lines.values():
            total_price += self.calculate_checkout_line_price(checkout_line)
        self.total_price = total_price

    def init_checkout_line(self, item_id):
        try:
            self.checkout_lines[item_id] = {
                **self.db["products"][item_id],
                "amount": 0
            }
        except KeyError:
            self.raise_http_error(
                Errors.ITEM_DOES_NOT_EXIST.format(item_id)
            )

    def raise_http_error(self, message):
        raise HTTPException(
            status_code=400,
            detail=message
        )

    @classmethod
    def calculate_checkout_line_price(cls, checkout_line):
        amount = checkout_line["amount"]
        unit_price = checkout_line["unit_price"]

        if "discount" not in checkout_line:
            return amount * unit_price

        discount = checkout_line["discount"]
        discount_amount_required = discount["amount_required"]
        discounted_price = discount["discounted_price"]

        num_of_applicable_discounts = amount // discount_amount_required
        discounted_items_price = num_of_applicable_discounts * discounted_price
        not_discounted_items_price = (amount % discount_amount_required) * unit_price

        return discounted_items_price + not_discounted_items_price
