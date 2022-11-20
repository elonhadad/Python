"""
Student: Elon Hadad
Assignment no. 1
Program: check_primes.py
"""

import random


def is_probably_prime(n):
    """
    The function will run "is_suspected_prime" 20 times
    if at all times True is returned, then "is_probably_prime" will return True.
    if False is returned at one time - the function will return False
    """

    for i in range(20):
        r_val = is_suspected_prime(n)
        if not r_val:
            return False
    return True


def is_suspected_prime(n):
    x = random.randint(2, n-1)
    y = (n-1) // 2
    result = modular_power(x, y, n)

    if result == 1 or result == n-1:
        return True
    return False


def modular_power(x, y, n):
    """
    Calculates the power mod n, (x(n-1) / 2)
    and returns the result to "is_suspected_prime"
    """
    lst = []
    while y > 0:
        if y % 2 == 1:
            lst = [1] + lst
        else:
            lst = [0] + lst
        y //= 2

    result = 1
    for k in lst:
        result = (result ** 2) % n
        if k == 1:
            result = (result * x) % n
    return result


def main():
    """
    The function will check for each number if it is prime using
    "is_probably_prime" function and print the numbers for
    the output_ex1.txt file and next to each number if it is prime or not
    """
    try:
        file = open('input.txt', 'r')
        f = file.readlines()
        file.close()

        num_lst = []
        sub_s = ''
        for i in f:
            for j in i:
                if j != '\n':
                    sub_s += j
                else:
                    num_lst.append(sub_s)
                    sub_s = ''

        new_f = open('output.txt', 'w')
        for n in num_lst:
            z = is_probably_prime(int(n))
            if z:
                new_f.write(f'{n} is prime \n')
            else:
                new_f.write(f'{n} is not prime \n')

    except FileNotFoundError:
        print('File not found, please make sure that "input.txt" in project folder')


if __name__ == '__main__':
    main()
