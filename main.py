#!usr/bin/env/ python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

from UI.UI import UI

if __name__ == "__main__":
    sudoku_board = [[0, 2, 0, 0, 0, 4, 3, 0, 0],
                    [9, 0, 0, 0, 2, 0, 0, 0, 8],
                    [0, 0, 0, 6, 0, 9, 0, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 7, 2, 5, 0, 3, 6, 8, 0],
                    [6, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 2, 0, 5, 0, 0, 0],
                    [1, 0, 0, 0, 9, 0, 0, 0, 3],
                    [0, 0, 9, 8, 0, 0, 0, 6, 0]]
    main_window = UI(sudoku_board)
    main_window.mainloop()