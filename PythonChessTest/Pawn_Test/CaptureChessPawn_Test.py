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
    def test_CaptureChessPiece_WhitePawn_LeftPiece(self):
        self.assertEqual(new_game.MoveChessPiece("dxc5"), True)
        self.assertIsInstance(new_board.board[4][2].chess_piece, ChessPython.WhitePawn)
        self.assertIsInstance(new_game.list_Chess_Pieces_White[0][0], ChessPython.WhitePawn)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "c5")
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 8)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 9)

    def test_CaptureChessPiece_WhitePawn_RightPiece(self):
        self.assertEqual(new_game.MoveChessPiece("dxe5"), True)
        self.assertIsInstance(new_board.board[4][4].chess_piece, ChessPython.WhitePawn)
        self.assertIsInstance(new_game.list_Chess_Pieces_White[0][0], ChessPython.WhitePawn)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "e5")
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 8)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 9)

    def test_CaptureChessPiece_WhitePawn_FrontPiece(self):
        self.assertEqual(new_game.MoveChessPiece("dxd5"), False)

    def test_CaptureChessPiece_WhitePawn_CaptureWhitePiece(self):
        self.assertEqual(new_game.MoveChessPiece("fxg5"), False)

    def test_CaptureChessPiece_WhitePawn_CaptureEmptySquare(self):
        self.assertEqual(new_game.MoveChessPiece("cxe4"), False)

    def test_CaptureChessPiece_WhitePawn_CaptureAndPromote(self):
        self.assertEqual(new_game.MoveChessPiece("bxa8"), False)

    def test_CaptureChessPiece_WhitePawn_IncorrectMoveCode(self):
        self.assertEqual(new_game.MoveChessPiece("d5"), False)

    def test_CaptureChessPiece_BlackPawn_RightPiece(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("cxd4"), True)
        self.assertIsInstance(new_board.board[3][3].chess_piece, ChessPython.BlackPawn)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackPawn)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "d4")
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 9)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 8)

    def test_CaptureChessPiece_BlackPawn_LeftPiece(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("exd4"), True)
        self.assertIsInstance(new_board.board[3][3].chess_piece, ChessPython.BlackPawn)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackPawn)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "d4")
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 9)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 8)

    def test_CaptureChessPiece_BlackPawn_InvalidCodeMove(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("hxe4"), False)

    def test_CaptureChessPiece_BlackPawn_InvalidTurn(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("exd5"), False)

print(new_game.board.printBoard())