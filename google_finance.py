import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import datetime


class GoogleFinance(object):

    def plot(self):
        data = sp.genfromtxt(r"data\EMG.csv", delimiter=",", usecols=(0, 1, 2, 3, 4, 5),
                             skip_header=1, dtype=int)
        days = data.__len__()
        print(days)
        data90 = np.reshape(data, (days, 6))#[::-1]
        x = np.arange(days)
        x90 = np.reshape(x, (days, 1))
        print(data90.shape)
        print(x90.shape)
        data2 = np.hstack((x90, data90))
        print(data2)
        x = data2[:, 0]
        y = data2[:, 2]
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]

        plt.scatter(x, y, s=2)
        plt.xticks(np.arange(min(x), max(x) + 1, 365), np.arange(min(x) / 365, (max(x) + 1) / 365, 1))
        plt.legend(["EMG.L"], loc="upper left")
        plt.grid(True, linestyle='-', color='0.75')
        plt.savefig("D:\plot.png")

        fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

        def error(f, x, y):
            return sp.sum((f(x) - y) ** 2)

        print("Model parameters: %s" % fp1)
        print(residuals)
        f1 = sp.poly1d(fp1)
        print(error(f1, x, y))

        fx = sp.linspace(0, x[-1], 1000)  # generate X-values for plotting
        plt.plot(fx, f1(fx), linewidth=2, color='green')
        plt.savefig("D:\plot_1.png")

        f2p = sp.polyfit(x, y, 2)
        f2 = sp.poly1d(f2p)
        plt.plot(fx, f2(fx), linewidth=2, color='yellow')
        plt.savefig("D:\plot_2.png")

        f10p = sp.polyfit(x, y, 10)
        f10 = sp.poly1d(f10p)
        plt.plot(fx, f10(fx), linewidth=2, color='red')
        plt.savefig("D:\plot_3.png")
