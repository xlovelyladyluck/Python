import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_array.search_array', return_value='7')
    def test_search_list_item_found(self, input):
        with self.assertEqual('7'):
            sort_and_search_array.search_array()

    @patch('fun_with_collections.sort_and_search_array.search_array', return_value='37')
    def test_search_list_item_not_found(self, input):
        with self.assertRaises(ValueError):
            sort_and_search_array.search_array()


if __name__ == '__main__':
    unittest.main()
