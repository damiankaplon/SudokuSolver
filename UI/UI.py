#!/usr/bin/env/ python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

import string
from tkinter import Tk, Button

from Solver.solver import solve


class UI(Tk):
    def __init__(self, board: list = None):
        super().__init__()
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.board: list = board
        self.title("Sudoku!")
        self.buttons: list = list()
        self.__create_main_board_buttons()
        self.__create_menu_buttons()

    def __create_main_board_buttons(self) -> None:
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board is not None:
                    text = self.board[i][j]
                else:
                    text = 0

                if text != 0:
                    self.__create_board_button(text, i, j, state="disabled")
                else:
                    self.__create_board_button(text, i, j)

    def __create_menu_buttons(self) -> None:
        button = Button(self, text="Solve", height=2, bd=2, font='sans 8 bold')
        button.bind("<Button-1>", self.__solve_button)
        button.grid(column=0, row=9, columnspan=9, sticky="nsew")
        self.buttons.append(button)

    def __load_values_from_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
                button = self.buttons[9*i+j]
                self.board[i][j] = int(button['text'])

    def __create_board_button(self, text: string, row: int, column: int, state="normal") -> None:
        button = Button(self, height=3, width=5, text=text, state=state, bd=1, fg="blue")
        button.bind("<Button-1>", self.__increment_button)
        button.grid(column=column, row=row)
        self.buttons.append(button)

    @staticmethod
    def __increment_button(event):
        state: string = event.widget['state']
        if state == "disabled":
            return
        text: string = (event.widget['text'])
        i: int = int(text)
        if i == 9:
            i = 1
        else:
            i += 1
        event.widget['text'] = i
        return

    def __solve_button(self, event):
        if event.widget['text'] == "Solve":
            self.__load_values_from_board()
            self.board = (solve(self.board))[1]
            for i in range(0, 9):
                for j in range(0, 9):
                    button = self.buttons[9*i+j]
                    button['text'] = self.board[i][j]
                    button['state'] = "disabled"
            return
        else:
            return
