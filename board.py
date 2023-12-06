from piece import Piece


class CheckersBoard:
	_board = [[None]*8 for i in range(8)]           # board
	
	def __init__(self):
		for i in range(3):
			for j in range(8):
				if (i + j) % 2 == 0:
					self._board[i][j] = Piece(2)
		for i in range(5, 8):
			for j in range(8):
				if (i + j) % 2 == 0:
					self._board[i][j] = Piece(1)

	def __str__(self):
		s = "=" * 32 + "\n"
		for i in range(8):
			s += "|"
			for j in range(8):
				if self._board[i][j] is None:
					s += "   |"
				else:
					s += str(self._board[i][j]).ljust(3) + "|"
			s += "\n" + "=" * 32 + "\n"
		return s
	
	def __repr__(self):
		s = ""
		for i in range(8):
			s += str(self._board[i]) + "\n"
		return s

if __name__ == "__main__":
	board = CheckersBoard()
	print(board)