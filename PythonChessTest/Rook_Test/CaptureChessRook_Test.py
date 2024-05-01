import ChessPython
import unittest 

new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "h1")

new_board.addChessPiece(ChessPython.BlackRook(), "a2")
new_board.addChessPiece(ChessPython.BlackRook(), "d1")
new_board.addChessPiece(ChessPython.BlackRook(), "e8")
new_board.addChessPiece(ChessPython.BlackRook(), "c5")
new_board.addChessPiece(ChessPython.BlackRook(), "a5")

new_board.addChessPiece(ChessPython.WhiteRook(), "f6")
new_board.addChessPiece(ChessPython.WhiteRook(), "g5")
new_board.addChessPiece(ChessPython.WhiteRook(), "h2")
new_board.addChessPiece(ChessPython.WhiteRook(), "b1")
new_board.addChessPiece(ChessPython.WhiteRook(), "d4")

new_board.addChessPiece(ChessPython.WhitePawn(), "a3")
new_board.addChessPiece(ChessPython.WhitePawn(), "b5")

new_board.addChessPiece(ChessPython.BlackPawn(), "f4")
new_board.addChessPiece(ChessPython.BlackPawn(), "d2")

new_game = ChessPython.Game(new_board)

class Test_CaptureChessRook(unittest.TestCase):

    def GeneralTestTrue(self, move_code, chess_piece, listChessPieceMove):
        column, row = move_code[-2:]
        indexColumn = ord(column) - 97
        indexRow = int(row)-1
        self.assertEqual(new_game.MoveChessPiece(move_code), True)
        self.assertIsInstance(new_game.board.board[indexRow][indexColumn].chess_piece, chess_piece)
        self.assertIsInstance(listChessPieceMove[0][0], chess_piece)
        self.assertEqual(listChessPieceMove[0][1], move_code[-2:])

    def test_CaptureChessRook_BlackRook_Left(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Rxb1", ChessPython.BlackRook, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessRook_BlackRook_Right(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Rxg1", ChessPython.BlackRook, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessRook_BlackRook_UpWith5Possition(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("R5xa3", ChessPython.BlackRook, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessRook_BlackRook_DownWith2Possition(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("R2xa3", ChessPython.BlackRook, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessRook_BlackRook_LeftWithaPossition(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Raxb5", ChessPython.BlackRook, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessRook_BlackRook_RightWithcPossition(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Rcxb5", ChessPython.BlackRook, new_game.list_Chess_Pieces_Black)

    def test_CaptureChessRook_BlackRook_Fail(self):
        new_game.MoveChessPiece("Kg1")
        test_variable ={
            ("Rxd4"),
            ("Rxh2"),
            ("Rxb2"),
            ("Rxb5"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

# print(new_game.board.printBoard())
