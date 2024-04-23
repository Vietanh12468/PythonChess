import ChessPython
import unittest 

new_board = ChessPython.Board()

class Test_CreateBoard(unittest.TestCase):
    def test_CreateBoard(self):
        self.assertEqual(new_board.board[0][0].tostring(), "a1")
        self.assertEqual(new_board.board[3][2].tostring(), "c4")
        self.assertEqual(new_board.board[7][7].tostring(), "h8")

class Test_AddChessPiece(unittest.TestCase):
    def test_AddChessPiece(self):
        blackKing = ChessPython.BlackKing()
        new_board.addChessPiece(blackKing, "a8")
        # assert the chess piece is == blackking object
        self.assertIsInstance(new_board.board[7][0].chess_piece, ChessPython.BlackKing)

blackKing = ChessPython.BlackKing()
new_board.addChessPiece(blackKing, "a8")
new_game = ChessPython.Game(new_board)

class Test_ShowAvailableMovesPiece(unittest.TestCase):
    def test_ShowAvailableMovesPiece(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('a8')), sorted(['b8', 'a7', 'b7']))
