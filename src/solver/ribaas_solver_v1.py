from engine.sudoku_board import SudokuBoard
from .i_sudoku_solver import ISudokuSolver


def find_missing_element (element_list):
  for i in range(1, 10):
    if not i in element_list:
      return i

class RibaasSudokuSolver (ISudokuSolver):
  # TODO: verbose solving
  def solve (self, board: SudokuBoard, deep_level = 0) -> object:
    while not board.is_board_complete():
      possible_numbers = {}

      for x in range(0, 9):
        for y in range(0, 9):
          if board.get_element_at(x, y) is None:
            possible_numbers[(x,y)] = []
            for i in range(1,10):
              board.set_element_at(x,y,i)
              if board.is_board_valid():
                possible_numbers[(x,y)].append(i)
            board.delete_element_at(x,y)

      # print(possible_numbers)

      stuck = True

      # strategy 1
      for key in possible_numbers:
        if len(possible_numbers[key]) == 1:
          board.set_element_at(key[0], key[1], possible_numbers[key][0])
          stuck = False

      # strategy 2a
      for i in range(0, 3):
        for j in range(0, 3):
          chunk_possible_numbers = {}
          for x in range(i*3 + 0, i*3 + 3):
            for y in range(j*3 + 0, j*3 + 3):
              if (x,y) in possible_numbers:
                chunk_possible_numbers[(x,y)] = possible_numbers[(x,y)]
          for number in range(1,10):
            possible_locations = []
            for key in chunk_possible_numbers:
              if number in chunk_possible_numbers[key]:
                possible_locations.append(key)
            if len(possible_locations) == 1:
              board.set_element_at(possible_locations[0][0], possible_locations[0][1], number)
              stuck = False

      # strategy 2b
      for x in range(0, 9):
        row_possible_numbers = {}
        for y in range(0, 9):
          if (x,y) in possible_numbers:
            row_possible_numbers[(x,y)] = possible_numbers[(x,y)]
        for number in range(1,10):
          possible_locations = []
          for key in row_possible_numbers:
            if number in row_possible_numbers[key]:
              possible_locations.append(key)
          if len(possible_locations) == 1:
            board.set_element_at(possible_locations[0][0], possible_locations[0][1], number)
            stuck = False

      # strategy 2c
      for y in range(0, 9):
        column_possible_numbers = {}
        for x in range(0, 9):
          if (x,y) in possible_numbers:
            column_possible_numbers[(x,y)] = possible_numbers[(x,y)]
        for number in range(1,10):
          possible_locations = []
          for key in column_possible_numbers:
            if number in column_possible_numbers[key]:
              possible_locations.append(key)
          if len(possible_locations) == 1:
            board.set_element_at(possible_locations[0][0], possible_locations[0][1], number)
            stuck = False

      if stuck:
        possible_numbers_pairs = {}
        # TODO: possible_solutions = []

        for key in possible_numbers:
          if len(possible_numbers[key]) == 2:
            possible_numbers_pairs[key] = possible_numbers[key]

        for key in possible_numbers_pairs:
          new_board_1 = SudokuBoard()
          new_board_1.set_initial_elements(board.get_elements())
          new_board_1.set_element_at(key[0], key[1], possible_numbers_pairs[key][0])
          self.solve(new_board_1, deep_level+1)
          if new_board_1.is_board_complete():
            for x in range(0,9):
              for y in range(0,9):
                if board.get_element_at(x,y) is None:
                  board.set_element_at(x, y, new_board_1.get_element_at(x, y))
            break

          new_board_2 = SudokuBoard()
          new_board_2.set_initial_elements(board.get_elements())
          new_board_2.set_element_at(key[0], key[1], possible_numbers_pairs[key][1])
          self.solve(new_board_2, deep_level+1)
          if new_board_2.is_board_complete():
            for x in range(0,9):
              for y in range(0,9):
                if board.get_element_at(x,y) is None:
                  board.set_element_at(x, y, new_board_2.get_element_at(x, y))
            break