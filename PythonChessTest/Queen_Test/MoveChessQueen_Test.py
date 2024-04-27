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

class Test_MoveChessQueen(unittest.TestCase):

    def test_MoveChessQueen_WhiteQueen_MoveInRow(self):
        self.assertEqual(new_game.MoveChessPiece("Qf1"), True)
        self.assertIsInstance(new_game.board.board[0][5].chess_piece, ChessPython.WhiteQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_White[0][0], ChessPython.WhiteQueen)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "f1")

    def test_MoveChessQueen_BlackQueen_MoveInDiagonal(self):
        new_game.MoveChessPiece("Qf1")
        self.assertEqual(new_game.MoveChessPiece("Qe3"), True)
        self.assertIsInstance(new_game.board.board[2][4].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "e3")

    def test_MoveChessQueen_BlackQueen_MoveInColumn(self):
        new_game.MoveChessPiece("Qf1")
        self.assertEqual(new_game.MoveChessPiece("Qh7"), True)
        self.assertIsInstance(new_game.board.board[6][7].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "h7")

    def test_MoveChessQueen_WhiteQueen_Fail(self):
        test_variable ={
            ("Qh1"),
            ("Qa2"),
            ("Qd2"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

    def test_MoveChessQueen_BlackQueen_Fail(self):
        new_game.MoveChessPiece("Qf1")
        test_variable ={
            ("Qb1"),
            ("Qf3"),
            ("Qc3"),
            ("Qh5"),
            ("Qf2"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

print(new_game.board.printBoard())
