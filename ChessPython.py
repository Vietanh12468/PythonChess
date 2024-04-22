from Interface.IChessPiece import *
from Interface.Color import *
from TransformPosition import *
from STATIC_VARIBLE import *
from Object.Board import *
from Object.Position import *

transformer = TransormPostion()

class BlackKing(IKing, Black):
    def __init__(self):
        IKing.__init__(self)
        Black.__init__(self)
        self.symbol = "♔ "

class WhiteKing(IKing, White):
    def __init__(self):
        IKing.__init__(self)
        White.__init__(self)
        self.symbol = "♚ "

class BlackQueen(IQueen, Black):
    def __init__(self):
        IQueen.__init__(self)
        Black.__init__(self)
        self.symbol = "♕ "

class WhiteQueen(IQueen, White):
    def __init__(self):
        IQueen.__init__(self)
        White.__init__(self)
        self.symbol = "♛ "

class WhitePawn(IPawn, White):
    def __init__(self):
        IPawn.__init__(self)
        White.__init__(self)
        self.symbol = "♟ "
    
class BlackPawn(IPawn, Black):
    def __init__(self):
        IPawn.__init__(self)
        Black.__init__(self)
        self.symbol = "♙ "


class Game:
    def __init__(self, board):
        self.board = board
        self.list_Chess_Pieces = []
        i = 0
        while i < 8:
            n = 0
            while n < 8:
                if self.board.board[i][n].chess_piece == None:
                    pass

                elif isinstance(self.board.board[i][n].chess_piece, IchessPiece):
                    # append the chess piece to the list with the position
                    self.list_Chess_Pieces.append((self.board.board[i][n].chess_piece, self.board.board[i][n].tostring()))
                n += 1
            i += 1

    # def ChessPieceSwitch(self, pie):
    #     match pie:
    #         case "k" :
    #             return ""

    def ShowAvailableMoves(self, chess_Piece):
        current_Postion = ""
        for piece in self.list_Chess_Pieces:
            # check if the chess piece class is the same
            if type(piece[0]) == type(chess_Piece):
                current_Postion = piece[1]
                break
        return chess_Piece.get_available_moves(current_Postion, self.board)
    
    def ShowChessPieceInfo(self, Postion):
        for piece in self.list_Chess_Pieces:
            if piece[1] == Postion:
                return piece[1] + ": " + piece[0].color + " " + piece[0].name + ", available moves: " + str(piece[0].get_available_moves(piece[1], self.board))
    
    def MoveChessPiece(self, move_Code):
        if len(move_Code) == 2:
            col, ro = move_Code[:2]
            for piece in self.list_Chess_Pieces:
                if piece[0].short_name == "P" and isinstance(piece[0], White):
                    if col + ro in piece[0].get_available_moves(piece[1], self.board):
                        old_Col, old_Row = piece[1][:2]
                        self.board.board[int(old_Row) - 1][transformer.tranformColumnToNumber(old_Col)].SetChessPiece(None)
                        self.board.board[int(ro)-1][transformer.tranformColumnToNumber(col)].SetChessPiece(piece[0])
                        self.list_Chess_Pieces.remove(piece)
        if len(move_Code) == 3:
            pie, col, ro = move_Code[:3]
            pie_Type = PieceSwitch().Switch(pie)
            piece_Index = 0
            for piece in self.list_Chess_Pieces:
                if isinstance(piece[0], pie_Type):
                    if piece[0].Move(piece[1], col, ro):
                        self.UpdateBoardAfterMove(piece[0], piece[1], col, ro, piece_Index)
                        return True
                piece_Index += 1
        print("Invalid move")
        return False
    
    def UpdateBoardAfterMove(self, Chess_Piece, old_Postion, new_Postion_Col, new_Postion_Row, piece_Index):
        old_Col, old_Row = old_Postion[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = transformer.tranformColumnToNumber(old_Col)
        index_New_Col = transformer.tranformColumnToNumber(new_Postion_Col)
        self.board.board[index_Old_Row][index_Old_Col].SetChessPiece(None)
        self.board.board[index_New_Row][index_New_Col].SetChessPiece(Chess_Piece)
        self.list_Chess_Pieces.pop(piece_Index) 
        self.list_Chess_Pieces.insert(0, (self.board.board[index_New_Row][index_New_Col].chess_piece, self.board.board[index_New_Row][index_New_Col].tostring()))
    

# Create a switch class for checking each piece short name
class PieceSwitch:
    def Switch(self, pie):
        match pie:
            case "K" :
                return IKing
            case "Q" :
                return IQueen
            case "R" :
                # return BlackRook()
                pass
            case "B" :
                # return BlackBishop()
                pass
            case "N" :
                # return BlackKnight()
                pass



    # def get_available_moves(self, current_position):
    #     list_Of_Available_Moves = []
    #     current_Column, current_Row = current_position[:2]
    #     for row in self.posible_Moves_Row_And_Column:
    #         for column in self.posible_Moves_Row_And_Column:
    #             if int(current_Row) + row in ROWS and chr(ord(current_Column.lower()) + column) in COLUMNS and not (row == 0 and column == 0):
    #                 list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
    #     return list_Of_Available_Moves


    # def BlackMove(self, move_Code):
    #     piece_Move = ""
    #     current_Postion = ""
    #     if move_Code.len() == 3:
    #         pie, col, ro = move_Code[:3]
    #         for piece in self.list_Chess_Pieces:
    #             # check if the chess piece class is the same
    #             if piece[0].short_name == pie and isinstance(piece[0], Black):
    #                 piece_Move = piece[0]
    #                 current_Postion = piece[1]
    #             ava

    def WhiteMove(self, chess_piece, position):
        pass

    # def generate_chess_pieces(self):
    #     for col in range(8):


