import unittest
from google_finance import GoogleFinance


class TddInPythonExample_Plotter(unittest.TestCase):

    def test_savepng(self):
        gf = GoogleFinance()
        gf.plot()

    def test_addidxcolumn(self):
        gf = GoogleFinance()
        reshaped = gf.addidxcolumn([
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407],
            [-1, 240, 239, 240, 231, 3260407]
        ],1)
        self.assertEqual(reshaped.shape, (9, 7))
        self.assertEqual(reshaped[5,0], 5)
