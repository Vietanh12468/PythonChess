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

class Test_PromotePawn(unittest.TestCase):
    def test_PromotePawn_WhitePawn_ToQueen(self):
        self.assertEqual(new_game.MoveChessPiece("b8=Q"), True)
        self.assertIsInstance(new_game.board.board[7][1].chess_piece, ChessPython.WhiteQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_White[0][0], ChessPython.WhiteQueen)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "b8")

    def test_PromotePawn_BlackPawn_ToQueen(self):
        new_game.MoveChessPiece("b8=Q")
        self.assertEqual(new_game.MoveChessPiece("f1=Q"), True)
        self.assertIsInstance(new_game.board.board[0][5].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "f1")
        
    def test_PromotePawn_WhitePawn_ToQueen_IncorrectMoveCode(self):
        self.assertEqual(new_game.MoveChessPiece("b8=K"), False)

    def test_PromotePawn_WhitePawn_ToQueen_IncorrectMoveCode2(self):
        self.assertEqual(new_game.MoveChessPiece("f1xQ"), False)

    def test_PromotePawn_WhitePawn_Capture_ToQueen(self):
        self.assertEqual(new_game.MoveChessPiece("bxa8=Q"), True)
        self.assertIsInstance(new_game.board.board[7][0].chess_piece, ChessPython.WhiteQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_White[0][0], ChessPython.WhiteQueen)
        self.assertEqual(new_game.list_Chess_Pieces_White[0][1], "a8")
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 8)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 9)

    def test_PromotePawn_BlackPawn_Capture_ToQueen(self):
        new_game.MoveChessPiece("Kg1")
        self.assertEqual(new_game.MoveChessPiece("fxg1=Q"), True)
        self.assertIsInstance(new_game.board.board[0][6].chess_piece, ChessPython.BlackQueen)
        self.assertIsInstance(new_game.list_Chess_Pieces_Black[0][0], ChessPython.BlackQueen)
        self.assertEqual(new_game.list_Chess_Pieces_Black[0][1], "g1")
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 9)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 8)

    def test_PromotePawn_WhitePawn_IncorrectMoveCode(self):
        self.assertEqual(new_game.MoveChessPiece("b8"), False)
    
    def test_PromotePawn_WhitePawn_IncorrectMoveCode2(self):
        self.assertEqual(new_game.MoveChessPiece("b=a8xQ"), False)

print(new_game.board.printBoard())