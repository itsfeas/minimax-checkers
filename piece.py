class Piece:
	_color = None          # color of piece. can be 1 (black) or 2 (white)
	_isKing = False        # is piece a king
	
	def __init__(self, color: int):
		self._color = color

	def __str__(self):
		s = "W" if self._color == 2 else "B"
		return s + ("+" if self._isKing else "")
	
	def __repr__(self):
		return f"[color: {self._color}, isKing: {self._isKing}]"
	
	def copy(self):
		new_piece = Piece(self._color)
		new_piece.set_isKing(self._isKing)
		return new_piece
	
	def get_color(self):
		return self._color
	
	def get_isKing(self):
		return self._isKing

	def set_color(self, color: int):
		self._color = color

	def set_isKing(self, isKing: bool):
		self._isKing = isKing