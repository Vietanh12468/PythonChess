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

class Test_MoveChessPawn(unittest.TestCase):
    def test_MoveChessPiece_WhitePawn_Jump2Move_inFirstMove(self):
        new_game.MoveChessPiece("b4")
        self.assertIsInstance(new_board.board[3][1].chess_piece, ChessPython.WhitePawn)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "b4")

    def test_MoveChessPiece_WhitePawn_1MoveForward_GetBlock(self):
        self.assertEqual(new_game.MoveChessPiece("d5"), False)

    def test_MoveChessPiece_WhitePawn_TakeOtherPiece_AllyColor(self):
        self.assertEqual(new_game.MoveChessPiece("g5"), False)

    def test_MoveChessPiece_WhitePawn_TakeOtherPiece_OpponentColor(self):
        self.assertEqual(new_game.MoveChessPiece("d5"), False)

    def test_MoveChessPiece_WhitePawn_1MoveForward_TryToPromote(self):
        self.assertEqual(new_game.MoveChessPiece("b8"), False)

    def test_MoveChessPiece_WhitePawn_Jump2Move_inFirstMove_GetBlock(self):
        self.assertEqual(new_game.MoveChessPiece("a4"), False)

    def test_MoveChessPiece_BlackPawn_Jump2Move_inFirstMove(self):
        new_game.MoveChessPiece("Kh2")
        new_game.MoveChessPiece("h5")
        self.assertIsInstance(new_board.board[4][7].chess_piece, ChessPython.BlackPawn)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "h5")

    def test_MoveChessPiece_BlackPawn_1MoveForward_Empty(self):
        new_game.MoveChessPiece("Kh2")
        new_game.MoveChessPiece("f5")
        self.assertIsInstance(new_board.board[4][5].chess_piece, ChessPython.BlackPawn)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "f5")

    def test_MoveChessPiece_BlackPawn_1MoveForward_TryToPromote(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("f1"), False)

    def test_MoveChessPiece_BlackPawn_1MoveForward_GetBlock(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("a2"), False)

    def test_MoveChessPiece_BlackPawn_TryToMoveBackward(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("b6"), False)

    def test_MoveChessPiece_BlackPawn_TakeOtherPiece(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("d4"), False)

    def test_MoveChessPiece_BlackPawn_Jump2Move_NotFirstMove(self):
        new_game.MoveChessPiece("Kh2")
        self.assertEqual(new_game.MoveChessPiece("b3"), False)

# print(new_game.board.printBoard())