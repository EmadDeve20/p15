#!/bin/env python3

def reset():
    """clear font color"""
    print("\033[0m")

def prnum(number):
    """this is function can be printing your number with private color"""
    try:
        number = int(number)
    except ValueError:
        print(f"this is {number} not a number! but recomend = 2")
        number = 1

    bold = '\033[01m'
    if number == 16:
        print(" \t" , end = '')
    else:
        print(bold+str(number)+'\t' , end = '')

def plist(numbers):
    """this function can be priting a numbers with private colors"""
    for i in range(len(numbers)):
        prnum(numbers[i])

def prmat(mat):
    """this is function can be priting matrix"""
    for i in range(len(mat)):
        plist(mat[i])
        print("");reset()
