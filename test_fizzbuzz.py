import unittest
from fizzbuzz import FizzBuzz


class TddInPythonExample_FizzBuzz(unittest.TestCase):

    def test_fizz_buzz_returns_1(self):
        fb = FizzBuzz()
        result = fb.get(1)
        self.assertEqual("1", result)

    def test_fizz_buzz_returns_3(self):
        fb = FizzBuzz()
        result = fb.get(3)
        self.assertEqual("Fizz", result)

    def test_fizz_buzz_returns_5(self):
        fb = FizzBuzz()
        result = fb.get(5)
        self.assertEqual("Buzz", result)

    def test_fizz_buzz_returns_15(self):
        fb = FizzBuzz()
        result = fb.get(15)
        self.assertEqual("FizzBuzz", result)

    def test_play(self):
        fb = FizzBuzz()
        result = fb.play(100)
        self.assertEqual(len(result), 100)

