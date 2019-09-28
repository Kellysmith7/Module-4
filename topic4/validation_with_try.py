"""
Program: validation_with_try.py
Author: Kelly Smith
Last date updated: 09/17/2019

Program to find the average of three numbers and returns a value error if a negative number is entered
"""


def average(x, y, z):
    if x < 0:
        raise ValueError
    elif y < 0:
        raise ValueError
    elif z < 0:
        raise ValueError
    scores = [x, y, z]
    return sum(scores) / len(scores)


if __name__ == '__main__':
    try:
        print(average(90, 95, -85))
    except ValueError:
        print("Number cannot be negative.")
    else:
        print("Average calculated.")
    finally:
        print("Code execution complete.")
