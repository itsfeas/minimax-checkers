class Piece:
	_pos = (None, None)    # coordinate (x, y)
	_color = None          # color of piece. can be 1 (black) or 2 (white)
	_isKing = False        # is piece a king
	
	def __init__(self, x: int, y: int, color: int):
		self._pos = (x, y)
		self._color = color

	def __str__(self):
		return f"[color: {self._color}, isKing: {self._color}, pos: {self._pos}]"
	
	def get_pos(self):
		return self._pos
	
	def get_x(self):
		return self._pos[0]
	
	def get_y(self):
		return self._pos[1]
	
	def get_color(self):
		return self._color
	
	def get_isKing(self):
		return self._isKing

	def set_x(self, x: int):
		self._pos[0] = x

	def set_y(self, y: int):
		self._pos[1] = y

	def set_pos(self, x: int, y: int):
		self._pos = (x, y)

	def set_color(self, color: int):
		self._color = color

	def set_isKing(self, isKing: bool):
		self._isKing = isKing