import unittest
from plotter import Plotter


class TddInPythonExample_Plotter(unittest.TestCase):

    def test_savepng(self):
        pl = Plotter()
        plt = pl.plot()


