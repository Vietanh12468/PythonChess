import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "h1")

new_board.addChessPiece(ChessPython.BlackKnight(), "d4")
new_board.addChessPiece(ChessPython.BlackKnight(), "d6")
new_board.addChessPiece(ChessPython.BlackKnight(), "g4")
new_board.addChessPiece(ChessPython.BlackKnight(), "f7")

new_board.addChessPiece(ChessPython.WhiteKnight(), "b3")
new_board.addChessPiece(ChessPython.WhiteKnight(), "g2")
new_board.addChessPiece(ChessPython.WhiteKnight(), "f1")
new_board.addChessPiece(ChessPython.WhiteKnight(), "f5")
new_board.addChessPiece(ChessPython.WhiteKnight(), "e5")
new_board.addChessPiece(ChessPython.WhiteKnight(), "c3")

new_board.addChessPiece(ChessPython.WhitePawn(), "a4")
new_board.addChessPiece(ChessPython.WhitePawn(), "b6")

new_board.addChessPiece(ChessPython.BlackPawn(), "f3")
new_board.addChessPiece(ChessPython.BlackPawn(), "d5")

new_game = ChessPython.Game(new_board)

class Test_CaptureChessKnight(unittest.TestCase):

    def GeneralTestTrue(self, move_code, chess_piece, listChessPieceMove):
        column, row = move_code[-2:]
        indexColumn = ord(column) - 97
        indexRow = int(row)-1
        self.assertEqual(new_game.MoveChessPiece(move_code), True)
        self.assertIsInstance(new_game.board.board[indexRow][indexColumn].chess_piece, chess_piece)
        self.assertIsInstance(listChessPieceMove[0][0], chess_piece)
        self.assertEqual(listChessPieceMove[0][1], move_code[-2:])

    def test_CaptureChessKnight_BlackKnight_With_f_Position(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Nfxe5", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessKnight_BlackKnight_With_g_Position(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Ngxe5", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessKnight_BlackKnight_With_4_Position(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("N4xf5", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessKnight_BlackKnight_With_6_Position(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("N6xf5", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessKnight_WhiteKnight_CaptureInDownRight(self):
        self.GeneralTestTrue("Nxd5", ChessPython.WhiteKnight, new_game.list_Chess_Pieces_White)

    def test_CaptureChessKnight_WhiteKnight_CaptureInUpRight(self):
        self.GeneralTestTrue("Nxf3", ChessPython.WhiteKnight, new_game.list_Chess_Pieces_White)

    def test_CaptureChessKnight_WhiteKnight_CaptureInDownLeft(self):
        self.GeneralTestTrue("Nxd6", ChessPython.WhiteKnight, new_game.list_Chess_Pieces_White)

    def test_CaptureChessKnight_WhiteKnight_Fail(self):
        test_variable ={
            ("Nxd4"),
            ("Nxa4"),
            ("Nxa6"),
            ("Nxf4"),
            ("Nexa8"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

# print(new_game.board.printBoard())