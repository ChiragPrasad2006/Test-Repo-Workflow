class ShoppingCart:
    def __init__(self):
        self.quantity = 0
    def add_item(self, quantity: int) -> None:
        self.quantity += quantity
    def get_total_cost(self) -> float:
        total = self.quantity * 100
        if total > 1000:
            total *= 0.9
        return float(total)
