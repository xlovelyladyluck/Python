import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='Black Cat')
    def test_search_list_item_found(self, input):
        with self.assertAlmostEqual('Black Cat'):
            sort_and_search_list.search_list()

    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='Pumpkin Pie')
    def test_search_list_item_not_found(self):
        with self.assertRaises(ValueError):
            sort_and_search_list.search_list()


if __name__ == '__main__':
    unittest.main()
