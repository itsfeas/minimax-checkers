class Piece:
	_pos = None, None      # coordinate (x, y)
	_color = None          # color of piece. can be 1 (black) or 2 (white)
	_isKing = False        # is piece a king
	
	def __init__(self, x: int, y: int, color: int):
		self._pos = (x, y)
		self._color = color

	def __str__(self):
		return f"[color: {self._color}, isKing: {self._color}, pos: ({self._pos[0]}, {self._pos[1]})]"