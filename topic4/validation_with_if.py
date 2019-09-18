"""
Program: validation_with_if.py
Author: Kelly Smith
Last date updated: 09/17/2019

Program to find the average of three numbers and return negative 1 if a negative is entered
"""


def average(x, y, z):
    if x < 0:
        return -1
    elif y < 0:
        return -1
    elif z < 0:
        return -1
    scores = [x, y, z]
    return sum(scores) / len(scores)


if __name__ == '__main__':
    print("Average Score: % 5.2f" % average(2, -3, 5))

