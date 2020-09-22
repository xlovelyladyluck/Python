import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

class test_price_under_10(unittest.TestCase):
    def testOne(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(15, 5, .1))
        self.assertAlmostEqual(coupon_calculations.calculate_order(10, 5, 10))
        self.assertAlmostEqual(coupon_calculations.calculate_order(12, 5, 20))
        self.assertAlmostEqual(coupon_calculations.calculate_order(10, 5, 20))




if __name__ == '__main__':
    unittest.main()
