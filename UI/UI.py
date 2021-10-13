#!/usr/bin/env/ python3.9
import string
from tkinter import Tk, Button


def onclick_button(event):
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


class UI(Tk):
    def __init__(self, board: list = None):
        super().__init__()
        self.board = board
        self.title("Sudoku!")
        self.buttons: list = list()
        self.__create_buttons()

    def __create_buttons(self) -> None:
        for i in range(0, 6):
            for j in range(0, 6):
                if self.board is not None:
                    text = self.board[i][j]
                else:
                    text = 0

                if text != 0:
                    self.__create_button(text, i, j, state="disabled")
                else:
                    self.__create_button(text, i, j)

    def __create_button(self, text: string, row: int, column: int, state: string = "normal") -> None:
        button = Button(self, height=5, width=5, text=text, state=state)
        button.bind("<Button-1>", onclick_button)
        button.grid(column=column, row=row)
        self.buttons.append(button)
