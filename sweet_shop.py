import json
import os

class SweetShop:
    def __init__(self, data_file='sweets_data.json'):
        self.data_file = data_file
        self.sweets = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.sweets = json.load(f)
        else:
            self.sweets = []

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.sweets, f, indent=4)

    def view_sweets(self):
        return self.sweets

    def delete_sweet(self, sweet_id):
        self.sweets = [s for s in self.sweets if s['id'] != sweet_id]
        self.save_data()

    def add_or_sell_sweet(self, id, name, category, price, quantity, action):
        found = False
        for sweet in self.sweets:
            if sweet['id'] == id:
                found = True
                if action == "add":
                    sweet['quantity'] += quantity
                elif action == "sell":
                    if sweet['quantity'] >= quantity:
                        sweet['quantity'] -= quantity
                    else:
                        raise ValueError("Not enough stock to sell.")
                break

        if not found:
            if action == "add":
                new_sweet = {
                    "id": id,
                    "name": name,
                    "category": category,
                    "price": price,
                    "quantity": quantity
                }
                self.sweets.append(new_sweet)
            else:
                raise ValueError("Sweet does not exist to sell.")
        self.save_data()
