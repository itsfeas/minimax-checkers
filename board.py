from collections import deque
from piece import Piece


class CheckersBoard:
	_board: list[list[Piece]]           # board
	
	def __init__(self):
		self._board = [[None]*8 for i in range(8)]

	def initial_board(self):
		for i in range(3):
			for j in range(8):
				if (i + j) % 2 == 0:
					self._board[i][j] = Piece(2)
		for i in range(5, 8):
			for j in range(8):
				if (i + j) % 2 == 0:
					self._board[i][j] = Piece(1)

	def __str__(self):
		s = "=" * 33 + "\n"
		for i in range(8):
			s += "|"
			for j in range(8):
				if self._board[i][j] is None:
					s += "   |"
				else:
					s += str(self._board[i][j]).ljust(3) + "|"
			s += "\n" + "=" * 33 + "\n"
		return s
	
	def __repr__(self):
		s = ""
		for i in range(8):
			s += str(self._board[i]) + "\n"
		return s
	
	def copy(self):
		new_board = CheckersBoard()
		for i in range(8):
			for j in range(8):
				if self._board[i][j]:
					new_board._board[i][j] = self._board[i][j].copy()
		return new_board
	
	def heuristic(self):
		return 0
	
	def generate_all_sucessors(self, color: int) -> deque['CheckersBoard']:
		sucessors = deque()
		for i in range(8):
			for j in range(8):
				if self._board[i][j] and self._board[i][j].get_color() == color:
					t = self.get_sucessors(i, j)
					if t: sucessors += t
		return sucessors

	def get_sucessors(self, i: int, j: int):
		if self._board[i][j] is None:
			return []
		all_moves = self.get_all_moves(i, j)
		sucessors = deque()
		for move in all_moves:
			is_possible, will_kill, new_pos, killed_pos = self.is_move_possible(i, j, move)
			print((i, j), is_possible, will_kill, new_pos, killed_pos)
			if not is_possible:
				continue
			new_board = self.copy()

			# if piece will be killed
			if will_kill:
				old_piece = new_board._board[i][j]
				new_board._board[killed_pos[0]][killed_pos[1]] = None
				new_board._board[new_pos[0]][new_pos[1]] = old_piece
				new_board.crown_if_necessary(new_pos[0], new_pos[1])
			else:
				# if no need to kill any piece
				new_board._board[new_pos[0]][new_pos[1]] = new_board._board[i][j]
				new_board.crown_if_necessary(new_pos[0], new_pos[1])
			new_board._board[i][j] = None
			sucessors.append(new_board)
		return sucessors

	def crown_if_necessary(self, i: int, j: int):
		# crowns piece if it achieves crowning conditions
		if self._board[i][j].get_isKing() or not self._board[i][j]: # if already king or empty
			return
		if (i == 7 and self._board[i][j].get_color()==2) or (i == 0 and self._board[i][j].get_color()==0):
			self._board[i][j].set_isKing(True)

	def is_move_possible(self, i: int, j: int, move: (int, int)):
		# returns (is move possible, is there a piece we jump over, (new i, new j), (killed i, killed j)
		new_i, new_j = i+move[0], j+move[1]

		# out of bounds
		if self.out_of_bounds(new_i, new_j):
			return (False, False, None, None)
		
		# if empty
		if self._board[new_i][new_j] is None:
			return (True, False, (new_i, new_j), None)
		
		# if diagonal piece is friendly
		if self._board[new_i][new_j].get_color() == self._board[i][j].get_color():
			return (False, False, None, None)
		
		killed = (new_i, new_j)
		new_i, new_j = i + 2*move[0], j+2*move[1]

		# out of bounds
		if self.out_of_bounds(new_i, new_j):
			return (False, False, None, None)
		
		# if kill jump is possible
		if self._board[new_i][new_j] is None:
			return (True, True, (i + 2*move[0], j+2*move[1]), killed)
		
		# kill jump is not possible
		return (False, False, None, None)
	
	def out_of_bounds(self, i: int, j: int):
		return (i < 0) or (i > 7) or (j < 0) or (j > 7)
	
	def get_all_moves(self, i: int, j: int):
		all_moves = deque()
		if self._board[i][j].get_color() == 1 or self._board[i][j].get_isKing():
			all_moves += deque([(-1, 1), (-1, -1)])
		if self._board[i][j].get_color() == 2 or self._board[i][j].get_isKing():
			all_moves += deque([(1, 1), (1, -1)])
		return all_moves

if __name__ == "__main__":
	board = CheckersBoard()
	print(board)