class Piece:
	_color = None          # color of piece. can be 1 (black) or 2 (white)
	_isKing = False        # is piece a king
	
	def __init__(self, color: int):
		self._color = color

	def __str__(self):
		s = "+" if self._isKing else ""
		return s + "W" if self._color == 2 else "B"
	
	def __repr__(self):
		return f"[color: {self._color}, isKing: {self._color}, pos: {self._pos}]"
	
	def get_color(self):
		return self._color
	
	def get_isKing(self):
		return self._isKing

	def set_color(self, color: int):
		self._color = color

	def set_isKing(self, isKing: bool):
		self._isKing = isKing