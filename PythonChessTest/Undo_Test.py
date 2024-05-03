import ChessPython
import unittest 

new_board = ChessPython.Board()
history = ChessPython.HistoryMoves()

new_board.addChessPiece(ChessPython.BlackRook(), "a8")
new_board.addChessPiece(ChessPython.BlackRook(), "h8")
new_board.addChessPiece(ChessPython.WhiteRook(), "a1")
new_board.addChessPiece(ChessPython.WhiteRook(), "h1")
new_board.addChessPiece(ChessPython.BlackKnight(), "b8")
new_board.addChessPiece(ChessPython.BlackKnight(), "g8")
new_board.addChessPiece(ChessPython.WhiteKnight(), "b1")
new_board.addChessPiece(ChessPython.WhiteKnight(), "g1")
new_board.addChessPiece(ChessPython.BlackBishop(), "c8")
new_board.addChessPiece(ChessPython.BlackBishop(), "f8")
new_board.addChessPiece(ChessPython.WhiteBishop(), "c1")
new_board.addChessPiece(ChessPython.WhiteBishop(), "f1")
new_board.addChessPiece(ChessPython.BlackQueen(), "d8")
new_board.addChessPiece(ChessPython.WhiteQueen(), "d1")
new_board.addChessPiece(ChessPython.BlackKing(), "e8")
new_board.addChessPiece(ChessPython.WhiteKing(), "e1")

new_board.addChessPiece(ChessPython.BlackPawn(), "a7")
new_board.addChessPiece(ChessPython.BlackPawn(), "b7")
new_board.addChessPiece(ChessPython.BlackPawn(), "c7")
new_board.addChessPiece(ChessPython.BlackPawn(), "d7")
new_board.addChessPiece(ChessPython.BlackPawn(), "e7")
new_board.addChessPiece(ChessPython.BlackPawn(), "f7")
new_board.addChessPiece(ChessPython.BlackPawn(), "g7")
new_board.addChessPiece(ChessPython.BlackPawn(), "h7")

new_board.addChessPiece(ChessPython.WhitePawn(), "a2")
new_board.addChessPiece(ChessPython.WhitePawn(), "b2")
new_board.addChessPiece(ChessPython.WhitePawn(), "c2")
new_board.addChessPiece(ChessPython.WhitePawn(), "d2")
new_board.addChessPiece(ChessPython.WhitePawn(), "e2")
new_board.addChessPiece(ChessPython.WhitePawn(), "f2")
new_board.addChessPiece(ChessPython.WhitePawn(), "g2")
new_board.addChessPiece(ChessPython.WhitePawn(), "h2")

new_game = ChessPython.Game(new_board)

new_game.MoveChessPiece("d4")
new_game.MoveChessPiece("d5")
new_game.MoveChessPiece("e4")
new_game.MoveChessPiece("e5")
new_game.MoveChessPiece("Nf3")
new_game.MoveChessPiece("Nf6")
new_game.MoveChessPiece("Nc3")
new_game.MoveChessPiece("Nc6")
new_game.MoveChessPiece("Bf4")
new_game.MoveChessPiece("Bf5")
new_game.MoveChessPiece("Bc4")
new_game.MoveChessPiece("Bc5")
new_game.MoveChessPiece("Nxe5")
new_game.MoveChessPiece("Nxe4")
new_game.MoveChessPiece("Nxe4")
new_game.MoveChessPiece("Nxe5")

class Test_UndoMoves(unittest.TestCase):
    def test_Undo1Moves(self):
        new_game.UndoMove()
        self.assertIsInstance(new_game.board.board[5][2].chess_piece, ChessPython.BlackKnight)
        self.assertIsInstance(new_game.board.board[4][4].chess_piece, ChessPython.WhiteKnight)

    def test_Undo2Moves(self):
        new_game.UndoMove()
        new_game.UndoMove()
        self.assertIsInstance(new_game.board.board[5][2].chess_piece, ChessPython.BlackKnight)
        self.assertIsInstance(new_game.board.board[4][4].chess_piece, ChessPython.WhiteKnight)
        self.assertIsInstance(new_game.board.board[2][2].chess_piece, ChessPython.WhiteKnight)
        self.assertIsInstance(new_game.board.board[3][4].chess_piece, ChessPython.BlackKnight)

    def test_Undo4Moves(self):
        new_game.UndoMove()
        new_game.UndoMove()
        new_game.UndoMove()
        new_game.UndoMove()
        self.assertIsInstance(new_game.board.board[3][4].chess_piece, ChessPython.WhitePawn)
        self.assertIsInstance(new_game.board.board[5][5].chess_piece, ChessPython.BlackKnight)
        self.assertIsInstance(new_game.board.board[4][4].chess_piece, ChessPython.BlackPawn)
        self.assertIsInstance(new_game.board.board[2][5].chess_piece, ChessPython.WhiteKnight)
    
    def test_UndoAll(self):
        i=0
        while i < 16:
            new_game.UndoMove()
            i+=1
        
        self.assertEqual(len(new_game.list_Chess_Pieces_Black), 16)
        self.assertEqual(len(new_game.list_Chess_Pieces_White), 16)
        self.assertIsNone(new_game.board.board[3][4].chess_piece)
        self.assertIsNone(new_game.board.board[4][4].chess_piece)
        self.assertIsNone(new_game.board.board[3][3].chess_piece)
        self.assertIsNone(new_game.board.board[4][3].chess_piece)
        self.assertIsInstance(new_game.board.board[0][1].chess_piece, ChessPython.WhiteKnight)
        self.assertIsInstance(new_game.board.board[0][2].chess_piece, ChessPython.WhiteBishop)
        self.assertIsInstance(new_game.board.board[6][3].chess_piece, ChessPython.BlackPawn)

# print(new_game.list_Chess_Pieces_White)
# print(len(new_game.list_Chess_Pieces_White))
# new_game.board.printBoard()