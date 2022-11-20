"""
Student: elon hadad
ID: 034672139
Assignment no. 2
Program: plot.py
"""
import matplotlib.pyplot as plt
from math import *


def plot(f, a, b, h=0.01):
    """
    Draw the graphs of The functions range from x = a to x = b.
    """
    x_vals = [a+i*h for i in range(int((b-a)/h))]
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals, y_vals, color='red')
    plt.xlabel("x")
    plt.ylabel("y")


def range_ab(f):
    """
    split the last line.
    :return: float number from last line.
    """
    a, b = (f[len(f) - 1].split())
    return float(a), float(b)


def eval_print(f):
    """
    Use the eval function to convert a string to a function.
    call to plot function
    """
    a, b = range_ab(f)
    for i in range(0, len(f)-1):
        x = eval('lambda x:' + f[i])
        plot(x, a, b)
    plt.show()


def main():
    file = open('functions.txt', 'r')
    f = file.read().splitlines()
    file.close()
    eval_print(f)
    range_ab(f)


if __name__ == "__main__":
    main()
