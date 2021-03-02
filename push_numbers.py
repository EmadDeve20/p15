#!/bin/env python3

"""
this Module can push matrix of game if event keys is True
"""

from typing import List

def can_pushing_left(mat: List[List[int]]):
    """we can pushing number to Left?"""

    for i in range(len(mat)):
        if mat[i][len(mat)-1] == 16:
            return False
    return True

def pushing_left(mat: List[List[int]]):
    """Now Pushint on the Left"""
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if mat[i][j] == 16:
                mat[i][j] = mat[i][j+1]
                mat[i][j+1] = 16
                return

def can_pushing_right(mat: List[List[int]]):
    """we can pushing number to Right?"""
    for i in range(len(mat)):
        if mat[i][0] == 16:
            return False
    return True

def pushing_right(mat: List[List[int]]):
    """Now Pushing on the Right"""
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 16:
                mat[i][j] = mat[i][j-1]
                mat[i][j-1] = 16
                return

def can_pushing_up(mat: List[List[int]]):
    """we can pushing number to Up?"""
    for i in range(len(mat)):
        if mat[len(mat)-1][i] == 16:
            return False

    return True

def pushing_up(mat: List[List[int]]):
    """Now pushing on the Up"""
    for i in range(len(mat)-1):
        for j in range(len(mat)):
            if mat[i][j] == 16:
                mat[i][j] = mat[i+1][j]
                mat[i+1][j] = 16
                return

def can_pushing_down(mat):
    """we can pushing number to Down?"""
    for i in range(len(mat)):
        if mat[0][i] == 16:
            return False
    return True


def pushing_down(mat: List[List[int]]):
    """Now Pushing on the down"""
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 16:
                mat[i][j] = mat[i-1][j]
                mat[i-1][j] = 16
                return

def matrix_is_alive(mat: List[List[int]]):
    """Game is finish or Not!"""
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if (mat[i][j]+1) != mat[i][j+1]:
                return True

    return False
