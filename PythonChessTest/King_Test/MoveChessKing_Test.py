import ChessPython
import unittest 
new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "c5")
new_board.addChessPiece(ChessPython.WhitePawn(), "d6")
new_board.addChessPiece(ChessPython.WhitePawn(), "c6")
new_board.addChessPiece(ChessPython.BlackPawn(), "b5")
new_board.addChessPiece(ChessPython.BlackPawn(), "b4")
new_game = ChessPython.Game(new_board)

class Test_MoveChessKing(unittest.TestCase):
    def test_MoveChessPiece_WhiteKing(self):
        new_game.MoveChessPiece("Kc4")
        self.assertIsInstance(new_board.board[3][2].chess_piece, ChessPython.WhiteKing)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "c4")

    def test_MoveChessPiece_BlackKing(self):
        new_game.MoveChessPiece("Kc4")
        new_game.MoveChessPiece("Kb8")
        self.assertIsInstance(new_board.board[7][1].chess_piece, ChessPython.BlackKing)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "b8")

    def test_MoveChessPiece_WhiteKing_Fail(self):
        self.assertEqual(new_game.MoveChessPiece("Kc6"), False)

    def test_MoveChessPiece_BlackKing_Fail(self):
        new_game.MoveChessPiece("Kc4")
        self.assertEqual(new_game.MoveChessPiece("Ka9"), False)

    def test_CaptureChessPiece_WhiteKing(self):
        new_game.MoveChessPiece("Kxb5")
        self.assertIsInstance(new_board.board[4][1].chess_piece, ChessPython.WhiteKing)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "b5")

    def test_CaptureChessPiece_WhiteKing1_Fail(self):
        self.assertEqual(new_game.MoveChessPiece("Kxc6"), False)


# print(new_game.board.printBoard())