from engine.sudoku_board import SudokuBoard
from engine.utils import validate_elements_matrix, get_empty_board_matrix, string_to_element_matrix


initial = """
398752106
106980070
020000009
003061000
904520013
015070000
700100698
400006037
650000000
"""

solved = """
398752146
146983275
527614389
873461952
964528713
215379864
732145698
481296537
659837421
"""

board = SudokuBoard()

board.print_board()
board.set_initial_elements(string_to_element_matrix(initial))
board.print_board()
print(board.is_board_valid())