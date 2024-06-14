from abc import abstractmethod, ABC
from engine.sudoku_board import SudokuBoard


class ISudokuSolver (ABC):
  @abstractmethod
  def solve (board: SudokuBoard) -> object:
    pass