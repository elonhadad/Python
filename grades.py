"""
Student: Elon Hadad
ID: 034672139
Assignment no. 2
Program: grades.py
"""
import sys


def read_students():
    """reads the data from the students.txt file and returns a dictionary
    where the keys are ID numbers and the values are the names of the students"""

    try:
        file = open('students.txt', 'r')
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    d_student = {}
    for line in file:
        try:
            key, val_1, val_2 = line.split()
            if len(key) != 9:
                print('Student ID is invalid')
                sys.exit()
        except ValueError:
            print('Missing name')
            sys.exit()
        d_student[key] = (val_1 + ' ' + val_2)
    file.close()
    return d_student


def read_grades():
    """Reads the data from the grades.txt file and returns a dictionary
    Where the keys are ID numbers and the values are lists of grades"""

    try:
        file = open('grades.txt', 'r')
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    d_grades = {}
    for line in file:
        lst = line.split()
        if len(lst) < 2:
            print("Missing grades")
            sys.exit()
        v = []
        for val in range(1, len(lst)):
            v.append(int(lst[val]))
        d_grades[lst[0]] = v
    file.close()
    return d_grades


def highest_avg(s, g):
    """print the student name with the highest grade average and his average"""
    best_avg = 0
    s_id = 0
    for val in g:
        avg = sum(g[val]) / len(g[val])
        if avg > best_avg:
            best_avg = avg
            s_id = val
    print(f'best student: {s[s_id]}, average: {best_avg:2.2f}')


def lst_grades(g):
    lst = []
    for value in g:
        for j in g[value]:
            lst.append(j)
    return lst


def most_comm(g, lst):
    """print the grade that received the most times"""

    most_t = ''
    cnt = 0
    for value in g:
        for j in g[value]:
            g_appear = lst.count(j)
            if g_appear > cnt:
                most_t = j
                cnt = g_appear
    set_2 = set()
    for val in lst:
        if lst.count(val) >= cnt:
            set_2.add(str(val))
    if len(set_2) == 1:
        print(f'the grade {most_t} appeared {cnt} times')
    elif len(set_2) > 1:
        print(f'the grades {",".join(set_2)} appeared {cnt} times')
    return lst


def other_grades(lst):
    """print the list of grades between 0 and 100 that did not appear at all"""

    other_g = set()
    for val in range(0, 101):
        if val not in lst:
            other_g.add(str(val))
    print(f'the grades that did not appear: {",".join(other_g)}')


def main():
    s = read_students()
    g = read_grades()
    highest_avg(s, g)
    lst = lst_grades(g)
    most_comm(g, lst)
    other_grades(lst)


if __name__ == '__main__':
    main()
