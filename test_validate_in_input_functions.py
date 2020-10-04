import unittest
from more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
   # def test_score_input_test_name(self):
       # self.assertAlmostEqual(validate_input_in_functions.score_input("Science", 0),"Science : 0")

   #def test_score_input_test_score_valid(self):
      # self.assertAlmostEqual(validate_input_in_functions.score_input("Science", 100), "Science : 100")

   # def test_score_input_test_score_below_range(self):
    #    self.assertAlmostEqual(validate_input_in_functions.score_input("Math", .011), "invalid literal for int() with base 10: '.011'")

    #def test_score_input_test_score_above_range(self):
     #   self.assertAlmostEqual(validate_input_in_functions.score_input("English", 125),"Invalid test score, Try again.")

    def test_test_score_non_numeric(self):
        self.assertAlmostEqual(validate_input_in_functions.score_input("French", "!!!"), "invalid literal for int() with base 10: '!!!' ", none)

   def test_test_score_input_invalid_message(self):
        self.assertAlmostEqual(validate_input_in_functions.score_input("French", -14), "Invalid test score, Try again.")



if __name__ == '__main__':
    unittest.main()
