from __future__ import annotations

class Cell():
	def __init__(self: object) -> None:
		"""
		Initializes a new instance of the Cell class.

		This constructor initializes the present, future, and neighbors attributes
		of the Cell object to their default values.

		Parameters:
		None

		Returns:
		None
		"""
		self.present = False
		self.future = False
		self.neighbors = None

	def present(self: object) -> bool:
		"""
		Checks if the object is alive.

		:param self: The object itself.
		:return: A boolean value indicating whether the object is alive or not.
		"""
		return self.present
	
	def set_neighbors(self: object, neighbors: list[Cell]) -> None:
		"""
		Sets the neighbors of the cell to the provided list of Cell objects.

		:param self: The object itself.
		:param neighbors: A list of Cell objects representing the neighbors of the cell.
		:return: None
		"""
		self.neighbors = neighbors

	def get_neighbors(self: object) -> list:
		"""
		Returns the list of neighbors of the object.

		:param self: The object itself.
		:return: A list of neighbors.
		"""
		return self.neighbors
	
	def born(self: object) -> None:
		"""
		Sets the future attribute of the cell to True.
		"""
		self.future = True

	def die(self: object) -> None:
		self.future = False
	
	def update(self: object) -> None:
		self.present = self.future
	
	def __str__(self: object) -> str:
		if self.present:
			return "X"
		else:
			return "-"
		
	def future_state_update(self: object) -> None:
		neighbors_alive = 0

		for neighbor_cell in self.get_neighbors():
			if neighbor_cell.present:
				neighbors_alive += 1

		if (neighbors_alive != 2) and (neighbors_alive != 3) and self.present:
			self.die()
		elif (neighbors_alive == 3) and not self.present:
			self.born()
		else:
			self.future = self.present