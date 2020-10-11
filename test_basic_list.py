import unittest
from fun_with_collections import basic_list
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='7')
    def test_list(self, input):
        self.assertEqual(basic_list.get_input(), '7')


if __name__ == '__main__':
    unittest.main()
