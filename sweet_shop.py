class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, id, name, category, price, quantity):
        sweet = {
            "id": id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }
        self.sweets.append(sweet)

    def view_sweets(self):
        return self.sweets
