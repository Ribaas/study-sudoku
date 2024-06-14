from engine.sudoku_board import SudokuBoard
from engine.utils import validate_elements_matrix, get_empty_board_matrix, string_to_element_matrix
from solver.ribaas_solver_v1 import RibaasSudokuSolver
from solver.test_boards import genius_initial


board = SudokuBoard()
board.set_initial_elements(string_to_element_matrix(genius_initial))
board.print_board()
print(f"Valid: {board.is_board_valid()}")

solver = RibaasSudokuSolver()
solver.solve(board)
board.print_board()

print(f"Valid: {board.is_board_valid()}")
print(f"Complete: {board.is_board_complete()}")