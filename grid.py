from __future__ import annotations
from cell import Cell
from random import random
class Grid():

	def __init__(self: object, rows: int, cols: int) -> None:
		self.rows = rows
		self.cols = cols
		self.matrix = self.set_matrix()
	
	def set_matrix(self: object) -> list[list[Cell]]:
		matrix = [[Cell() for j in range(self.cols)]
				   for i in range(self.rows)]
		return matrix
	

	def in_grid(self: object, i: int, j: int) -> bool:
		return 0 <= j < self.cols and 0 <= i < self.rows

	def set_cell_xy(self: object, i: int, j: int, cell: Cell) -> None:
		if self.in_grid(i, j):
			self.matrix[i][j] = cell
		else:
			raise IndexError(f"({i}, {j}) not in the grid")

	def get_cell_xy(self: object, i: int, j: int) -> Cell:
		if self.in_grid(i, j):
			return self.matrix[i][j]
		else:
			raise IndexError(f"({i}, {j}) not in the grid")

	def get_cols(self: object) -> int:
		return self.cols

	def get_rows(self: object) -> int:
		return self.rows

	@staticmethod
	def is_neighbor(i: int, j: int, x: int, y: int) -> bool:
		return (abs(x - i) == 1) or (abs(y - j) == 1)

	def get_neighbors(self: object, x: int, y: int) -> list[Cell]:
		neighbors = []
		for i in range(x - 1, x + 2):
			for j in range(y - 1, y + 2):
				if self.in_grid(i, j) and Grid.is_neighbor(x, y, i, j):
					neighbors.append(self.get_cell_xy(i, j))
		return neighbors

	def set_neighbors(self: object) -> None:
		for i in range(self.rows):
			for j in range(self.cols):
				cell = self.get_cell_xy(i, j)
				cell.set_neighbors(self.get_neighbors(i, j))

	def __str__(self: object) -> str:
		string = ""
		for i in range(self.rows):
			for j in range(self.cols):
				string += str(self.get_cell_xy(i, j)) + " "
			string += "\n"
		return string

	def random_fill(self, rate: int) -> None:
		for i in range(self.rows):
			for j in range(self.cols):
				if random() <= (rate / 100):
					cell = self.get_cell_xy(i, j)
					cell.born()
					cell.update()
	def game(self: object) -> None:
		for i in range(self.rows):
			for j in range(self.cols):
				cell = self.get_cell_xy(i, j)
				cell.future_state_update()

	def refresh(self: object) -> None:
		for i in range(self.rows):
			for j in range(self.cols):
				cell = self.get_cell_xy(i, j)
				cell.update()


if __name__ == "__main__":
	grid = Grid(4, 5)
	print(grid)