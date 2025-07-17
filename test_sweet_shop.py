import unittest
import os
from sweet_shop import SweetShop

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_sweets_data.json'
        # Clear any existing test data
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.shop = SweetShop(data_file=self.test_file)

    def test_add_sweet(self):
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 10, "add")
        sweets = self.shop.view_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0]['quantity'], 10)

    def test_add_existing_sweet(self):
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 10, "add")
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 5, "add")
        self.assertEqual(self.shop.view_sweets()[0]['quantity'], 15)

    def test_sell_sweet(self):
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 10, "add")
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 4, "sell")
        self.assertEqual(self.shop.view_sweets()[0]['quantity'], 6)

    def test_sell_more_than_available(self):
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 5, "add")
        with self.assertRaises(ValueError):
            self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 10, "sell")

    def test_restock_sweet(self):
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 2, "add")
        self.shop.add_or_sell_sweet(1001, "Kaju Katli", "Nut-Based", 50, 13, "add")
        self.assertEqual(self.shop.view_sweets()[0]['quantity'], 15)

if __name__ == '__main__':
    unittest.main()
