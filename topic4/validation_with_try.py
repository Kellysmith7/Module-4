"""
Program: validation_with_try.py
Author: Kelly Smith
Last date updated: 09/17/2019

Program to find the average of three numbers and return negative 1 if a negative is entered
"""


def average(x, y, z):
    scores = [x, y, z]
    return sum(scores) / len(scores)


if __name__ == '__main__':
    print("Average Score: % 5.2f" % average())