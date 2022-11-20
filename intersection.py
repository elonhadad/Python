"""
Student: elon hadad
Assignment no. 1
Program: intersection.py
"""
from math import *
from random import *
import sys


def newton_raphson(f, epsilon=10 ** (-10), n=100, h=0.000001):
    """
    Newton Rapson's method for finding the 0 point of a function
    """
    deriv = lambda x: (f(x + h) - f(x)) / h
    x0 = uniform(0.1, 10)
    while abs(deriv(x0)) < epsilon:
        x0 = uniform(0.1, 10)
    x = x0
    y = f(x)
    count = 1

    while abs(y) > epsilon and count <= n:
        count += 1
        y = f(x)
        x = x - y/deriv(x)

    if count > n:
        return None
    return x


def func_diff(f, g):
    """
    The function receives two functions `g` and `f`.
    :return: Difference between The first function to the second function.
    """
    return lambda x: f(x) - g(x)


def main():
    try:
        lst = []
        file = open("input.txt", "r")
        for val in file.readlines():
            lst.append(val)
        file.close()

        my_range = lst[2].split()
        f = eval(f"lambda x: {lst[0]}")
        g = eval(f"lambda x: {lst[1]}")

        flag = True
        for i in range(50):
            try:
                for j in range(50):
                    root = newton_raphson(func_diff(f, g))
                    if float(my_range[0]) < root < float(my_range[1]):
                        print(f"intersection: ({root:.4f} ,{f(root):.4f})")
                        sys.exit()
                flag = False
            except ValueError:
                continue
        if flag:
            print("no intersection")
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()
