from piece import Piece


class CheckersBoard:
	_board = [[None]*8 for i in range(8)]           # board
	
	def __init__(self):
		for i in range(3):
			for j in range(8):
				if (j) % 2:
					self._board[i][j] = Piece(i, j, 1)
		for i in range(5, 8):
			for j in range(8):
				if (j + 1) % 2 == 0:
					self._board[i][j] = Piece(i, j, 2)

	def __str__(self):
		s = "=" * 24 + "\n"
		for i in range(8):
			t = "|"
			for j in range(8):
				if self._board[i][j] is None:
					s += "  "
				else:
					s += "{2f}|".format(str(self._board[i][j]))
			s += t + "|\n"
			s += str(self._board[i]) + "\n"
		return s + "=" * 24 + "\n"
	
	def __repr__(self):
		s = ""
		for i in range(8):
			s += str(self._board[i]) + "\n"
		return s

if __name__ == "__main__":
	board = CheckersBoard()
	print(board)