import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "h1")

new_board.addChessPiece(ChessPython.BlackBishop(), "a1")
new_board.addChessPiece(ChessPython.BlackBishop(), "c1")
new_board.addChessPiece(ChessPython.BlackBishop(), "h7")
new_board.addChessPiece(ChessPython.BlackBishop(), "g2")
new_board.addChessPiece(ChessPython.BlackBishop(), "d7")

new_board.addChessPiece(ChessPython.WhiteBishop(), "b1")
new_board.addChessPiece(ChessPython.WhiteBishop(), "h8")
new_board.addChessPiece(ChessPython.WhiteBishop(), "f1")
new_board.addChessPiece(ChessPython.WhiteBishop(), "e2")
new_board.addChessPiece(ChessPython.WhiteBishop(), "e3")
new_board.addChessPiece(ChessPython.WhiteBishop(), "b6")

new_board.addChessPiece(ChessPython.WhitePawn(), "a2")
new_board.addChessPiece(ChessPython.WhitePawn(), "b2")

new_board.addChessPiece(ChessPython.BlackPawn(), "a3")
new_board.addChessPiece(ChessPython.BlackPawn(), "f2")

new_game = ChessPython.Game(new_board)

class Test_CaptureChessBishop(unittest.TestCase):

    def test_CaptureChessBishop_BlackBishop_CaptureInUpLeft(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Bxf1"), True)
        self.assertIsInstance(new_game.board.board[0][5].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "f1")

    def test_CaptureChessBishop_BlackBishop_CaptureInUpRight(self):
        new_game.MoveChessPiece("Ba7")
        self.assertEqual(new_game.MoveChessPiece("Bxh1"), True)
        self.assertIsInstance(new_game.board.board[0][7].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "h1")

    def test_CaptureChessBishop_BlackBishop_CaptureInDownLeft(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Baxb2"), True)
        self.assertIsInstance(new_game.board.board[1][1].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "b2")

    def test_CaptureChessBishop_BlackBishop_CaptureInDownRight(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Bcxb2"), True)
        self.assertIsInstance(new_game.board.board[1][1].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "b2")

    def test_CaptureChessBishop_WhiteBishop_Fail(self):
        test_variable ={
            ("Bxa2"),
            ("Bxa1"),
            ("Bxa7"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

    def test_CaptureChessBishop_BlackBishop_Fail(self):
        new_game.MoveChessPiece("Kg1")
        test_variable ={
            ("Bxb2"),
            ("Bxh8"),
            ("Bxa8"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

# print(new_game.board.printBoard())
