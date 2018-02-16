import unittest
from google_finance import GoogleFinance


class TddInPythonExample_Plotter(unittest.TestCase):

    def test_savepng(self):
        googlefinance = GoogleFinance()
        googlefinance.plot()
