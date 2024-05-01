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

class Test_MoveChessRook(unittest.TestCase):

    def GeneralTestTrue(self, move_code, chess_piece, listChessPieceMove):
        column, row = move_code[-2:]
        indexColumn = ord(column) - 97
        indexRow = int(row)-1
        self.assertEqual(new_game.MoveChessPiece(move_code), True)
        self.assertIsInstance(new_game.board.board[indexRow][indexColumn].chess_piece, chess_piece)
        self.assertIsInstance(listChessPieceMove[0][0], chess_piece)
        self.assertEqual(listChessPieceMove[0][1], move_code[-2:])

    def test_MoveChessRook_WhiteRook_Up(self):
        self.GeneralTestTrue("Rd3", ChessPython.WhiteRook, new_game.list_Chess_Pieces_White)

    def test_MoveChessRook_WhiteRook_Down(self):
        self.GeneralTestTrue("Rd7", ChessPython.WhiteRook, new_game.list_Chess_Pieces_White)

    def test_MoveChessRook_WhiteRook_Left(self):
        self.GeneralTestTrue("Ra4", ChessPython.WhiteRook, new_game.list_Chess_Pieces_White)

    def test_MoveChessRook_WhiteRook_Right(self):
        self.GeneralTestTrue("Re4", ChessPython.WhiteRook, new_game.list_Chess_Pieces_White)

    def test_MoveChessRook_WhiteRook_Fail(self):
        test_variable ={
            ("Rf5"),
            ("Nd5"),
            ("Rf3"),
            ("Ra7"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

# print(new_game.board.printBoard())