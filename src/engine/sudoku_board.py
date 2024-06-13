from .utils import get_empty_board_matrix, validate_coordinates, validate_element, clone_elements_matrix, validate_elements_matrix


class SudokuBoard:

  # list of rows / x -> row / y -> column
  __elements: list[list[int]] = get_empty_board_matrix()

  __initial_elements: list[list[int]] = get_empty_board_matrix()
  __initial_elements_set: bool = False

  def __init__(self):
    pass

  def set_initial_elements(self, initial_elements: list[list[int]]):
    if self.__initial_elements_set:
      raise Exception("Initial elements already set")
    validate_elements_matrix(initial_elements)

    self.__elements = clone_elements_matrix(initial_elements)
    self.__initial_elements_set = True

  def is_initial_elements_set (self) -> bool:
    return self.__initial_elements_set

  def print_board (self, pretty : bool = True, empty_char : str = " ") -> str:
    text = ""

    if pretty:
      for x in range (0, 3):
        for y in range (0, 3):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "| "
        for y in range (3, 6):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "| "
        for y in range (6, 9):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "\n"
      text += "------+-------+------\n"
      for x in range (3, 6):
        for y in range (0, 3):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "| "
        for y in range (3, 6):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "| "
        for y in range (6, 9):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "\n"
      text += "------+-------+------\n"
      for x in range (6, 9):
        for y in range (0, 3):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "| "
        for y in range (3, 6):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "| "
        for y in range (6, 9):
          text += (str(self.__elements[x][y]) if self.__elements[x][y] else empty_char) + " "
        text += "\n"
    else:
      for row in self.__elements:
        row_text = ""
        for element in row:
          if element:
            row_text += element
          else:
            row_text += empty_char
        text += row_text + "\n"

    print(text)

  def get_element_at (self, x: int, y: int) -> int:
    validate_coordinates(x,y)

    return self.__elements[x][y]

  def set_element_at (self, x: int, y: int, element):
    validate_coordinates(x,y)
    validate_element(element)

    if element is None:
      self.delete_element_at(x, y)
      return

    self.__elements[x][y] = element

  def delete_element_at (self, x: int, y: int, force_delete: bool = False):
    validate_coordinates(x,y)

    if not force_delete and self.__initial_elements[x][y]:
      raise Exception(f"[{x},{y}] position is an initial element")

    self.__elements[x][y] = None

  def is_board_valid(self) -> bool:

    for x in range(0, 9):
      row = []
      for y in range(0, 9):
        if self.__elements[x][y]:
          row.append(self.__elements[x][y])
      if len(row) != len(set(row)):
        return False

    for y in range(0, 9):
      column = []
      for x in range(0, 9):
        if self.__elements[x][y]:
          column.append(self.__elements[x][y])
      if len(column) != len(set(column)):
        return False

    for i in range(0, 3):
      for j in range(0, 3):
        chunk = []
        for x in range(i*3 + 0, i*3 + 3):
          for y in range(j*3 + 0, j*3 + 3):
            if self.__elements[x][y]:
              chunk.append(self.__elements[x][y])
        if len(chunk) != len(set(chunk)):
          return False

    return True