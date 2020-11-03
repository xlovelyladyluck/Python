import unittest
import Student as t

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person = t.Student('Reid', 'Spencer')

    def tearDown(self):
        del self.Student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.Student.last_name, 'Reid')
        self.assertEqual(self.Student.first_name, 'Spencer')

    def test_inital_all_attributes(self):
        student = t.Student('Reid', 'Spencer', 'Math', '4.0')
        assert student.last_name == 'Reid'
        assert student.first_name == 'Spencer'
        assert student.major == 'Math'
        assert student.gpa == '4.0'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = t.Student('123', 'Spencer')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            s = t.Student('Reid', '123')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = t.Student('Reid', 'Spencer', '23=32-')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = t.Student('Reid', 'Spencer', 'Math', 'abc')

if __name__ == '__main__':
    unittest.main()
