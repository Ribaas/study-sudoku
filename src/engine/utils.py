import re


empty_board_matrix: list[list[int]] = [[None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None]]

def clone_elements_matrix (matrix: list[list[int]]) -> list[list[int]]:
  return [[i for i in row] for row in matrix]

def get_empty_board_matrix () -> list[list[int]]:
  return clone_elements_matrix(empty_board_matrix)

def is_valid_coordinate (coordinate: int) -> bool:
  return 0 <= coordinate and coordinate <= 8

def validate_x (x: int):
  if not is_valid_coordinate(x):
    raise Exception("X should be a number from 0 to 8")

def validate_y (y: int):
  if not is_valid_coordinate(y):
    raise Exception("Y should be a number from 0 to 8")

def validate_coordinates (x: int, y: int):
  validate_x(x)
  validate_y(y)

def is_valid_number (number: int) -> bool:
  return 1 <= number and number <= 9

def is_valid_element (element) -> bool:
  return element is None or (type(element) is int and is_valid_number(element))

def validate_element(element):
  if not is_valid_element(element):
    raise Exception("Element should be a number from 1 to 9 or None")

def validate_elements_matrix (matrix: list[list[int]]):
  if len(matrix) != 9:
    raise Exception("Matrix should have exactly 9 rows")

  for x in range (0,9):
    row = matrix[x]
    if len(row) != 9:
      raise Exception(f"Matrix row {x} has {len(row)} columns, should be 9")

    for y in range (0,9):
      element = row[y]
      if not is_valid_element(element):
        raise Exception(f"Element \"{element}\" at [{x},{y}] is invalid, should be a number from 1 to 9 or None")

def string_to_element_matrix (input_string: str) -> list[list[int]]:
  input_string = re.sub(r"[^0-9\s]+", "0", input_string)
  input_array = input_string.split()

  elements_matrix : list[list[int]] = []

  if len(input_array) == 9:
    for x in range(0,9):
      row = re.sub(r"[^0-9]+", "", input_array[x])

      if len(row) != 9:
        raise Exception("Invalid input string")

      elements_matrix.append([])

      for element in row:
        elements_matrix[x].append(int(element) if element != "0" else None)

  elif len(input_array) == 81:
    # TODO: implement input string
    raise Exception("Not implemented yet")
  else:
    raise Exception("Invalid input string")

  validate_elements_matrix(elements_matrix)
  return elements_matrix
