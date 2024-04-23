import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "h1")

new_board.addChessPiece(ChessPython.WhitePawn(), "a2")
new_board.addChessPiece(ChessPython.WhitePawn(), "b2")
new_board.addChessPiece(ChessPython.WhitePawn(), "c3")
new_board.addChessPiece(ChessPython.WhitePawn(), "d4")
new_board.addChessPiece(ChessPython.WhitePawn(), "e4")
new_board.addChessPiece(ChessPython.WhitePawn(), "f4")
new_board.addChessPiece(ChessPython.WhitePawn(), "g5")
new_board.addChessPiece(ChessPython.WhitePawn(), "b7")

new_board.addChessPiece(ChessPython.BlackPawn(), "a3")
new_board.addChessPiece(ChessPython.BlackPawn(), "b5")
new_board.addChessPiece(ChessPython.BlackPawn(), "c5")
new_board.addChessPiece(ChessPython.BlackPawn(), "d5")
new_board.addChessPiece(ChessPython.BlackPawn(), "e5")
new_board.addChessPiece(ChessPython.BlackPawn(), "f6")
new_board.addChessPiece(ChessPython.BlackPawn(), "f2")
new_board.addChessPiece(ChessPython.BlackPawn(), "h7")

new_game = ChessPython.Game(new_board)

class Test_CaptureChessPawn(unittest.TestCase):
    def test_CaptureChessPiece_WhitePawn(self):
        self.assertEqual(new_game.MoveChessPiece("d5"), False)


print(new_game.board.printBoard())