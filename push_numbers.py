#!/bin/env python3

def can_pushing_left(mat):
    """we can pushing number to left?"""
    for i in range(len(mat)):
        if mat[i][len(mat)-1] == 16:
            return False
    return True

def pushing_left(mat):
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if mat[i][j] == 16:
                mat[i][j] = mat[i][j+1]
                mat[i][j+1] = 16
                return 0

def can_pushing_right(mat):
    """we can pushing number to right?"""
    for i in range(len(mat)):
        if mat[i][0] == 16:
            return False
    return True

def pushing_right(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 16:
                mat[i][j] = mat[i][j-1]
                mat[i][j-1] = 16
                return 0

def can_pushing_up(mat):
    """we can pushing number to up?"""
    for i in range(len(mat)):
        if mat[len(mat)-1][i] == 16:
            return False

    return True

def pushing_up(mat):
    for i in range(len(mat)-1):
        for j in range(len(mat)):
            if mat[i][j] == 16:
                mat[i][j] = mat[i+1][j]
                mat[i+1][j] = 16
                return 0

def can_pushing_down(mat):
    """we can pushing number to down?"""
    for i in range(len(mat)):
        if mat[0][i] == 16:
            return False
    return True


def pushing_down(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 16:
                mat[i][j] = mat[i-1][j]
                mat[i-1][j] = 16
                return 0


def matrix_is_alive(mat):
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if mat[i][j]+1 ==  mat[i][j+1]:
                return True

    return False
