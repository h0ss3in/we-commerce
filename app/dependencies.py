class CheckoutHandler:

    def __init__(self, items: list[str]):
        self.item_ids = items
        self.items = []
        self.total_price = 0

    def create(self):
        # TODO: create the checkout
        self.total_price = 360
