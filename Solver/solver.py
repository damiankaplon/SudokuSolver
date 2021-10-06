#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"


def find_empty(board: list) -> list:
    """returns position of next empty place in board. If board has no empty place returns list which contains False"""
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):
            if board[i][j] == 0:
                return [i, j]
    return [False]


def solve(board: list) -> list:
    pass
