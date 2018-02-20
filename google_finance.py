import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


class GoogleFinance(object):

    def plot(self):
        self.getdataandplot("EMG",2)
        self.getdataandplot("FTSE",2)

    def getdataandplot(self, source, idx):
        datasource = self.getdata(r"data\\" + source + ".csv")
        datasource = np.reshape(datasource, (datasource.__len__(), 6))  # [::-1]
        datasource = self.addidxcolumn(datasource, 1)
        x, y = self.splitintoxy(datasource, idx)
        self.plotit(x, y, source)
        self.linspaceit(x, y, 10, 'red')
        plt.savefig("D:\\" + source + ".png")
        plt.clf()

    def getdata(self, filename):
        print(filename)
        return sp.genfromtxt(filename, delimiter=",", usecols=(0, 1, 2, 3, 4, 5), skip_header=1, dtype=int)

    def addidxcolumn(self, data, seed):
        print(data)
        days = data.__len__()
        idx = np.arange(seed-1, days+(seed-1))
        idx = np.reshape(idx, (days, 1))
        return np.hstack((idx, data))

    def plotit(self, x, y, label):
        plt.plot(x, y)
        divisor = max(x) / 7
        plt.xticks(np.arange(min(x), max(x) + 1, divisor), np.arange(min(x) / divisor, (max(x) + 1) / divisor, 1))
        plt.legend([label], loc="upper left")
        plt.grid(True, linestyle='-', color='0.75')

    def splitintoxy(self, data, idx):
        x = data[:, 0]
        y = data[:, idx]
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]
        return x, y

    def linspaceit(self, x, y, deg, color):
        fx = sp.linspace(0, x[-1], 1000)  # generate X-values for plotting
        f10p = sp.polyfit(x, y, deg)
        f10 = sp.poly1d(f10p)
        plt.plot(fx, f10(fx), linewidth=2, color=color)


