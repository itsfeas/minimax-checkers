from board import CheckersBoard

class CheckersMiniMax:
	def get_move(self, board: CheckersBoard, d: int) -> int:
		pass

	# def __traverse(self, board: CheckersBoard, d: int):
	# 	for 

	def __get_all_moves(self, board: CheckersBoard, color: int, d: int):
		return board.generate_all_sucessors(color)
		

if __name__ == "__main__":
	board = CheckersBoard()
	board.initial_board()
	print(board)
	s = board.generate_all_sucessors(1)[0]
	print(s)
	s = s.generate_all_sucessors(2)[0]
	print(s)