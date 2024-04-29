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

class Test_MoveChessBishop(unittest.TestCase):

    def test_MoveChessBishop_BlackBishop_MoveInUpLeft(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Bb5"), True)
        self.assertIsInstance(new_game.board.board[4][1].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "b5")

    def test_MoveChessBishop_BlackBishop_MoveInUpRight(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Bg4"), True)
        self.assertIsInstance(new_game.board.board[3][6].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "g4")

    def test_MoveChessBishop_BlackBishop_MoveInDownLeft(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Bc8"), True)
        self.assertIsInstance(new_game.board.board[7][2].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "c8")

    def test_MoveChessBishop_BlackBishop_MoveInDownRight(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("Be8"), True)
        self.assertIsInstance(new_game.board.board[7][4].chess_piece, ChessPython.BlackBishop)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackBishop)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "e8")

    def test_MoveChessBishop_WhiteBishop_Fail(self):
        test_variable ={
            ("Bd4"),
            ("Bb7"),
            ("Be2"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

    def test_MoveChessBishop_BlackBishop_Fail(self):
        new_game.MoveChessPiece("Kg1")
        test_variable ={
            ("Bd8"),
            ("Ba6"),
            ("Ba7"),
            ("Bb2"),
            ("Ba3"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

# print(new_game.board.printBoard())
