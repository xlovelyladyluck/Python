import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEquals(string_functions.multiply_string(), "taylortaylortaylortaylortaylortaylortaylor")


if __name__ == '__main__':
    unittest.main()
