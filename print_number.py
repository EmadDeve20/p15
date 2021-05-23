#!/bin/env python3

"""
This Module for print Matrix of Game
--------------
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15
--------------
"""

from typing import List


def reset():
    """clear font color"""
    print("\033[0m")

def prnum(number: int):
    """this is function can be printing your number with private color"""
    try:
        number = int(number)
    except ValueError:
        print(f"this is {number} not a number! but recomend = 2")
        number = 1

    bold = '\033[01m'
    if number == 16:
        print(" \t", end='')
    else:
        print(bold+str(number)+'\t', end='')

def plist(numbers: List[int]):
    """this function can be priting a numbers with private colors"""
    for i in range(len(numbers)):
        prnum(numbers[i])

def prmat(mat: List[List[int]]):
    """this is function can be priting matrix"""
    print("\n" * 10)
    for i in range(len(mat)):
        print("\t" * 7, end = "")
        plist(mat[i])
        print("")
        reset()
