import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
# new_board.addChessPiece(ChessPython.WhiteKing(), "c5")
new_board.addChessPiece(ChessPython.WhitePawn(), "d6")
new_board.addChessPiece(ChessPython.WhitePawn(), "c6")
new_board.addChessPiece(ChessPython.BlackPawn(), "b5")
new_board.addChessPiece(ChessPython.BlackPawn(), "b4")
new_game = ChessPython.Game(new_board)

class Test_ShowAvailableMovesPiece(unittest.TestCase):
    def test_ShowAvailableMovesPiece_BlackKing(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves(ChessPython.BlackKing())), sorted(['b8', 'a7', 'b7']))
    
    # def test_ShowAvailableMovesPiece_WhiteKing(self):
    #     self.assertListEqual(sorted(new_game.ShowAvailableMoves(ChessPython.WhiteKing())), sorted(['b4', 'b5', 'b6', 'c4', 'd4', 'd5']))

class Test_MoveChessPiece(unittest.TestCase):
    def test_MoveChessPiece_BlackKing(self):
        new_game.MoveChessPiece("Kb8")
        self.assertIsInstance(new_board.board[7][1].chess_piece, ChessPython.BlackKing)

# class Test_MoveChessPiece(unittest.TestCase):
#     def test_MoveChessPiece_WhiteKing(self):
#         new_game.MoveChessPiece("Kb8")
#         self.assertEqual(new_board.board[7][1].chess_piece, None)