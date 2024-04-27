import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "h1")

new_board.addChessPiece(ChessPython.WhiteQueen(), "a1")
new_board.addChessPiece(ChessPython.BlackQueen(), "f1")
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

class Test_CaptureChessQueen(unittest.TestCase):
    def test_CaptureChessQueen_WhiteQueen_CaptureInRow(self):
        self.assertEqual(new_game.MoveChessPiece("Qxf1"), True)
        self.assertIsInstance(new_game.board.board[0][5].chess_piece, ChessPython.WhiteQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_White[0][0], ChessPython.WhiteQueen)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "f1")

    def test_CaptureChessQueen_BlackQueen_Fail(self):
        new_game.MoveChessPiece("Kg1")
        test_variable ={
            ("Qxa4"),
            ("Qxe1"),
            ("Qxh1"),
            ("Qxf1"),
            }
        
        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

    def test_CaptureChessQueen_WhiteQueen_Fail(self):
        test_variable ={
            ("Qxc3"),
            ("Qxa3"),
            ("Qxe1"),
            ("Qxg1"),
            }
        
        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)


    def test_CaptureChessQueen_BlackQueen_CaptureInDiagonal(self):
        new_game.MoveChessPiece("Qxf1")
        self.assertEqual(new_game.MoveChessPiece("Qxc2"), True)
        self.assertIsInstance(new_game.board.board[1][2].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "c2")

    def test_CaptureChessQueen_BlackQueen_CaptureInColumn(self):
        new_game.MoveChessPiece("Qxf1")
        self.assertEqual(new_game.MoveChessPiece("Qxb2"), True)
        self.assertIsInstance(new_game.board.board[1][1].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "b2")


    def test_CaptureChessQueen_BlackQueen_WithAdditionalInfo(self):
        new_game.MoveChessPiece("Qe1")
        self.assertEqual(new_game.MoveChessPiece("Qaxa4"), True)
        self.assertIsInstance(new_game.board.board[3][0].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "a4")

print(new_game.board.printBoard())