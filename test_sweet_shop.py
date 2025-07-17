import unittest
from sweet_shop import SweetShop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        shop.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        sweets = shop.view_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0]['name'], "Kaju Katli")

if __name__ == '__main__':
    unittest.main()
