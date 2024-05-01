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

class Test_MoveChessKnight(unittest.TestCase):

    def GeneralTestTrue(self, move_code, chess_piece, listChessPieceMove):
        column, row = move_code[-2:]
        indexColumn = ord(column) - 97
        indexRow = int(row)-1
        self.assertEqual(new_game.MoveChessPiece(move_code), True)
        self.assertIsInstance(new_game.board.board[indexRow][indexColumn].chess_piece, chess_piece)
        self.assertIsInstance(listChessPieceMove[0][0], chess_piece)
        self.assertEqual(listChessPieceMove[0][1], move_code[-2:])

    def test_MoveChessKnight_BlackKnight_MoveInUpLeft(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Nc6", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_MoveChessKnight_BlackKnight_MoveInUpRight(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Nc2", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_MoveChessKnight_BlackKnight_MoveInDownLeft(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Ne6", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_MoveChessKnight_BlackKnight_MoveInDownRight(self):
        new_game.MoveChessPiece("Kg1")
        self.GeneralTestTrue("Ne2", ChessPython.BlackKnight, new_game.list_Chess_Pieces_Black)

    def test_MoveChessKnight_WhiteKnight_MoveInUpLeft(self):
        self.GeneralTestTrue("Nc4", ChessPython.WhiteKnight, new_game.list_Chess_Pieces_White)

    def test_MoveChessKnight_WhiteKnight_MoveIndownLeft(self):
        self.GeneralTestTrue("Nc6", ChessPython.WhiteKnight, new_game.list_Chess_Pieces_White)
    
    def test_MoveChessKnight_WhiteKnight_MoveIndownRight(self):
        self.GeneralTestTrue("Ng6", ChessPython.WhiteKnight, new_game.list_Chess_Pieces_White)

    def test_MoveChessKnight_BlackKnight_Fail(self):
        new_game.MoveChessPiece("Kg1")
        test_variable ={
            ("Nb5"),
            ("Nc7"),
            ("Nb3"),
            ("Nd7"),
        }

        for move_code in test_variable:
            with self.subTest(move_code=move_code):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, False)

# print(new_game.board.printBoard())