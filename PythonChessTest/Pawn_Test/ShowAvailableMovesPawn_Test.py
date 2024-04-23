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

class Test_ShowAvailableMovesPawn(unittest.TestCase):
    def test_ShowAvailableMovesPiece_WhitePawn_a2(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('a2')), sorted([]))

    def test_ShowAvailableMovesPiece_WhitePawn_b2(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('b2')), sorted(['b3', 'b4', 'bxa3']))

    def test_ShowAvailableMovesPiece_WhitePawn_d4(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('d4')), sorted(['dxc5', 'dxe5']))

    def test_ShowAvailableMovesPiece_WhitePawn_b7(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('b7')), sorted(['b8=?', 'bxa8=?']))

    def test_ShowAvailableMovesPiece_BlackPawn_h7(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('h7')), sorted(['h6', 'h5']))

    def test_ShowAvailableMovesPiece_BlackPawn_e5(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('e5')), sorted(['exd4', 'exf4']))

    def test_ShowAvailableMovesPiece_BlackPawn_a3(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('a3')), sorted(['axb2']))
    
    def test_ShowAvailableMovesPiece_BlackPawn_f2(self):
        self.assertListEqual(sorted(new_game.ShowAvailableMoves('f2')), sorted(['f1=?']))

print(new_game.board.printBoard())