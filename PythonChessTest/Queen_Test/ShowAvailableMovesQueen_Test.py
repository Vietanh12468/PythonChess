import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "h1")

new_board.addChessPiece(ChessPython.WhiteQueen(), "a1")
new_board.addChessPiece(ChessPython.BlackQueen(), "a7")
new_board.addChessPiece(ChessPython.BlackQueen(), "b3")

new_board.addChessPiece(ChessPython.WhitePawn(), "a2")
new_board.addChessPiece(ChessPython.WhitePawn(), "b2")
new_board.addChessPiece(ChessPython.WhitePawn(), "c2")
new_board.addChessPiece(ChessPython.WhitePawn(), "a4")
new_board.addChessPiece(ChessPython.WhitePawn(), "b4")

new_board.addChessPiece(ChessPython.BlackPawn(), "a3")
new_board.addChessPiece(ChessPython.BlackPawn(), "f2")
new_board.addChessPiece(ChessPython.BlackPawn(), "c4")
new_board.addChessPiece(ChessPython.BlackPawn(), "c3")

new_game = ChessPython.Game(new_board)

class Test_ShowAvailableMovesQueen(unittest.TestCase):

    def test_ShowAvailableMovesPiece_Queen(self):
        test_cases = [
            ("a1", ['b1', 'c1', 'd1', 'e1', 'f1', 'g1']),
            ("a7", ['b8', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'b6', 'c5', 'd4', 'e3', 'a6', 'a5', 'Qxa4']),
            ("b3", ['Qxb4', 'Qxa4', 'Qxc2', 'Qxb2', 'Qxa2']),
        ]
        for position, expected_result in test_cases:
            with self.subTest(position=position, expected_result=expected_result):
                actual_result = new_game.ShowAvailableMoves(position)
                self.assertListEqual(sorted(actual_result), sorted(expected_result))