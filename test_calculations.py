import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

class test_price(unittest.TestCase):
    def test_price_under_10(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9,5,10))
        self.assertAlmostEqual(coupon_calculations.calculate_price(10, 5, 10))
        self.assertAlmostEqual(coupon_calculations.calculate_price(2, 5, 20))
        self.assertAlmostEqual(coupon_calculations.calculate_price(2, 10,20))
    def test_price_over_10_under_30(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(15, 10, 15))
        self.assertAlmostEqual(coupon_calculations.calculate_price(20,10,15))
        self.assertAlmostEqual(coupon_calculations.calculate_price(29,5,10))
    def test_price_over_30_50(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10,20))
        self.assertAlmostEqual(coupon_calculations.calculate_price(50, 5, 15))
        self.assertAlmostEqual(coupon_calculations.calculate_price(36, 5, 10))








if __name__ == '__main__':
    unittest.main()
