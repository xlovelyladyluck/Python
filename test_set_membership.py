import unittest
from more_fun_with_collections import set_membership

class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(True, set_membership.in_set("1"))

    def test_in_set_false(self):
        self.assertEqual(False, set_membership.in_set("fairy"))


if __name__ == '__main__':
    unittest.main()
