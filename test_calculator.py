import unittest
from calculator import Calculator


class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_add_method_returns_correct_result_for_strings(self):
        calc = Calculator()
        result = calc.add("Lee", "Barnard")
        self.assertEqual("LeeBarnard", result)

    def test_calculator_add_method_returns_correct_result_for_string_and_int(self):
        calc = Calculator()
        result = calc.add("Lee", "1")
        self.assertEqual("Lee1", result)
