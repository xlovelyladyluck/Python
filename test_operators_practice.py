import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        a = 5
        b = 4
        self.assertFalse(a == b)

    def test_not_equals(self):
        a = 3
        b = 3
        self.assertFalse(a != b)

    def test_greater_than(self):
        a = 3
        b = 1
        self.assertTrue(a > b)

    def test_less_than(self):
        a = 4
        b = 7
        self.assertTrue(a < b)


def test_greater_than(self):
    a = 3
    b = 3
    self.assertEqual(a >= b)


def test_less_than(self):
    a = 5
    b = 6
    self.assertTrue(a <= b)


if __name__ == '__main__':
    unittest.main()
