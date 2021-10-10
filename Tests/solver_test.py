#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

from unittest import TestCase
from Solver.solver import *


class SolverTest(TestCase):
    def setUp(self) -> None:
        self.sudoku_board = [[0, 2, 0, 0, 0, 4, 3, 0, 0],
                             [9, 0, 0, 0, 2, 0, 0, 0, 8],
                             [0, 0, 0, 6, 0, 9, 0, 5, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [0, 7, 2, 5, 0, 3, 6, 8, 0],
                             [6, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 8, 0, 2, 0, 5, 0, 0, 0],
                             [1, 0, 0, 0, 9, 0, 0, 0, 3],
                             [0, 0, 9, 8, 0, 0, 0, 6, 0]]

        self.correct_solution = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
                                 [9, 6, 5, 3, 2, 7, 1, 4, 8],
                                 [3, 4, 1, 6, 8, 9, 7, 5, 2],
                                 [5, 9, 3, 4, 6, 8, 2, 7, 1],
                                 [4, 7, 2, 5, 1, 3, 6, 8, 9],
                                 [6, 1, 8, 9, 7, 2, 4, 3, 5],
                                 [7, 8, 6, 2, 3, 5, 9, 1, 4],
                                 [1, 5, 4, 7, 9, 6, 8, 2, 3],
                                 [2, 3, 9, 8, 4, 1, 5, 6, 7]]

    def test_solve(self) -> None:
        solver_solution: list = solve(self.sudoku_board)
        self.assertEqual(self.correct_solution, solver_solution)

    def test_find_empty1(self) -> None:
        self.assertEqual(False, find_empty(self.correct_solution)[0])

    def test_find_empty2(self) -> None:
        self.assertEqual([0, 0], find_empty(self.sudoku_board))

    def test_find_empty3(self) -> None:
        some_sudoku_board = [[1, 2, 3, 4],
                             [1, 2, 3, 5],
                             [6, 9, 8, 0]]
        self.assertEqual([2, 3], find_empty(some_sudoku_board))

    def test_check_value(self) -> None:
        some_sudoku_board = [[0, 2, 0, 0, 0, 4, 3, 0, 0],
                             [9, 2, 0, 0, 2, 0, 0, 0, 8],
                             [0, 0, 0, 6, 0, 9, 0, 5, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [0, 7, 2, 5, 0, 3, 6, 8, 0],
                             [6, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 8, 0, 2, 0, 5, 0, 0, 0],
                             [1, 0, 0, 0, 9, 0, 0, 0, 3],
                             [0, 0, 9, 8, 0, 0, 0, 6, 0]]
        self.assertEqual(False, check_value(some_sudoku_board, 4, 4, 5))

    def test_check_value2(self) -> None:
        some_sudoku_board = [[5, 2, 1, 7, 0, 4, 3, 0, 0],
                             [9, 0, 0, 0, 2, 0, 0, 0, 8],
                             [0, 0, 0, 6, 0, 9, 0, 5, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [0, 7, 2, 5, 0, 3, 6, 8, 0],
                             [6, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 8, 0, 2, 0, 5, 0, 0, 0],
                             [1, 0, 0, 0, 9, 0, 0, 0, 3],
                             [0, 0, 9, 8, 0, 0, 0, 6, 0]]
        self.assertEqual(False, check_value(some_sudoku_board, 0, 4, 6))
