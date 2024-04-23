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

class Test_ShowAvailableMovesKing(unittest.TestCase):
    def test_ShowAvailableMovesPiece_BlackKing(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('a8')), sorted(['b8', 'a7', 'b7']))
    
    def test_ShowAvailableMovesPiece_WhiteKing(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('c5')), sorted(['Kxb4', 'Kxb5', 'b6', 'c4', 'd4', 'd5']))

# print(new_game.board.printBoard())