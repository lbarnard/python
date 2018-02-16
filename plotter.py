import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


class Plotter(object):

    def plot(self):
        data = sp.genfromtxt("H:\SampleData\web_traffic.tsv", delimiter="\t")
        print(data)
        print(data.shape)
        x = data[:, 0]
        y = data[:, 1]
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]

        plt.scatter(x, y, s=2)
        plt.xticks([w*7*24 for w in range(10)],
                   ['week %i' % w for w in range(10)])
        plt.autoscale(tight=True)
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
        plt.legend(["d=%i" % f1.order], loc="upper left")
        plt.savefig("D:\plot_1.png")

        f2p = sp.polyfit(x, y, 2)
        f2 = sp.poly1d(f2p)
        plt.plot(fx, f2(fx), linewidth=2, color='red')
        plt.legend(["d=%i" % f2.order], loc="upper left")
        plt.savefig("D:\plot_2.png")

        f10p = sp.polyfit(x, y, 10)
        f10 = sp.poly1d(f10p)
        plt.plot(fx, f10(fx), linewidth=2, color='yellow')
        plt.legend(["d=%i" % f10.order], loc="upper left")
        plt.savefig("D:\plot_3.png")