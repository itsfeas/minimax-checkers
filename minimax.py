from board import CheckersBoard

class CheckersMiniMax:
	_board: CheckersBoard           # board
	
	def __init__(self):
		self._board = CheckersBoard()

	def __str__(self):
		return self._board
	
	def __repr__(self):
		return self._board