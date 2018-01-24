import unittest
import numpy as np
from fibonacci import Fibonacci


class TddInPythonExample_Fibonacci(unittest.TestCase):

    def test_fibonacci_returns_1(self):
        fib = Fibonacci()
        result = fib.calculate(100)
        self.assertEqual(0, result[0])
        self.assertEqual(1, result[1])

        my_array2 = np.genfromtxt('d:\data.txt',
                                  skip_header=1,
                                  filling_values=-999,)

        print(my_array2)



