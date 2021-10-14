#!/usr/bin/env/ python3.9
import string
from tkinter import Tk, Button

from Solver.solver import solve


def increment_button(event):
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

def solve_button(event, board: list):
    
    return solve(board)


class UI(Tk):
    def __init__(self, board: list = None):
        super().__init__()
        self.board = board
        self.title("Sudoku!")
        self.rowconfigure(9)
        self.buttons: list = list()
        self.__create_main_board_buttons()

    def __create_main_board_buttons(self) -> None:
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board is not None:
                    text = self.board[i][j]
                else:
                    text = 0

                if text != 0:
                    self.__create_main_board_button(text, i, j, state="disabled")
                else:
                    self.__create_main_board_button(text, i, j)
        self.__create_menu_buttons()

    def __create_menu_buttons(self) -> None:
        button = Button(self, height=3, width=5, text="Solve", bd=4)
        button.bind("<Button-1>", solve_button(self.board))
        button.grid(column=7, row=10, columnspan=2)
        self.buttons.append(button)

    def __create_main_board_button(self, text: string, row: int, column: int, state: string = "normal") -> None:
        button = Button(self, height=3, width=5, text=text, state=state, bd=4)
        button.bind("<Button-1>", increment_button)
        button.grid(column=column, row=row)
        self.buttons.append(button)
