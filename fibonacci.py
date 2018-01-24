import numpy as np


class Fibonacci(object):

    def calculate(self, x):
        result = [0, 1]
        for i in range(2, x):
            result.append(result[i-2] + result[i-1])

        return result

