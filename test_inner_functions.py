import unittest
from more_functions import inner_functions_assignment

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(inner_functions_assignment.measurements(2.1,3.4), "Perimeter = 11.0 Area = 7.14")


if __name__ == '__main__':
    unittest.main()
