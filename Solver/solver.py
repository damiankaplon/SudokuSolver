#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"


def find_empty(board: list) -> list or bool:
    """returns position of next empty place in board. If board has no empty place returns list which contains False"""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i, j]
    return False


def solve(board: list) -> bool and list:
    empty = find_empty(board)
    if not empty:
        return True, board

    row, column = empty
    for i in range(1, 10):
        if check_value(board, row, column, i):
            board[row][column] = i
            if solve(board):
                return True, board

            board[row][column] = 0
    return False


def check_value(board: list, row: int, column: int, value: int) -> bool:
    if value in board[row]:
        return False

    for i in range(len(board)):
        if value == board[i][column]:
            return False

    x = row // 3
    y = column // 3

    for i in range(0, 3):
        for j in range(0, 3):
            if value == board[i + 3 * x][j + 3 * y]:
                return False

    return True
