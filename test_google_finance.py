import unittest
from google_finance import GoogleFinance


class TddInPythonExample_Plotter(unittest.TestCase):

    def test_savepng(self):
        googlefinance = GoogleFinance()
        data = googlefinance.load_yahoo_quote('AAPL', '20170515', '20170517')
        print(data)
