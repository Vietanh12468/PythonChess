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
        self.list_Chess_Pieces_White = []
        self.list_Chess_Pieces_Black = []
        self.numberOfMoves = 0
        i = 0
        while i < 8:
            n = 0
            while n < 8:
                this_Chess_Piece = self.board.board[i][n].chess_piece
                this_Position = self.board.board[i][n].tostring()
                if this_Chess_Piece == None:
                    pass
                elif isinstance(this_Chess_Piece, IchessPiece) and isinstance(this_Chess_Piece, White):
                    self.list_Chess_Pieces.append((this_Chess_Piece, this_Position))
                    self.list_Chess_Pieces_White.append((this_Chess_Piece, this_Position))
                elif isinstance(this_Chess_Piece, IchessPiece) and isinstance(this_Chess_Piece, Black):
                    self.list_Chess_Pieces.append((this_Chess_Piece, this_Position))
                    self.list_Chess_Pieces_Black.append((this_Chess_Piece, this_Position))
                n += 1
            i += 1

    def current_Turn(self):
        if self.numberOfMoves % 2 == 0:
            return "White"
        else:
            return "Black"

    # def ShowAvailableMoves(self, chess_Piece):
    #     current_Postion = ""
    #     for piece in self.list_Chess_Pieces:
    #         if type(piece[0]) == type(chess_Piece):
    #             current_Postion = piece[1]
    #             break
    #     return chess_Piece.get_available_moves(current_Postion, self.board)
    
    def ShowChessPieceInfo(self, Postion):
        for piece in self.list_Chess_Pieces:
            if piece[1] == Postion:
                return piece[1] + ": " + piece[0].color + " " + piece[0].name + ", available moves: " + str(piece[0].get_available_moves(piece[1], self.board))
    
    # Fixing and Adding Required
    def MoveChessPiece(self, move_Code):
        if self.current_Turn() == "White":
            this_Turn_Chess_Pieces_List = self.list_Chess_Pieces_White
        else:
            this_Turn_Chess_Pieces_List = self.list_Chess_Pieces_Black

        if len(move_Code) == 2:
            col, ro = move_Code[:2]
            piece_Index = 0
            for piece in this_Turn_Chess_Pieces_List:
                if isinstance(piece[0], IPawn):
                    if piece[0].Move(piece[1], col, ro, self.board):
                        self.UpdateBoardAfterMove(piece[0], piece[1], col, ro, piece_Index)
                        return True
                    
        elif len(move_Code) == 3:
            pie, col, ro = move_Code[:3]
            pie_Type = PieceSwitch().Switch(pie)
            piece_Index = 0
            for piece in this_Turn_Chess_Pieces_List:
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
        if self.current_Turn == "White":
            self.list_Chess_Pieces_White.pop(piece_Index)
            self.list_Chess_Pieces_White.insert(0, (Chess_Piece, new_Postion_Col + new_Postion_Row))
        else:
            self.list_Chess_Pieces_Black.pop(piece_Index)
            self.list_Chess_Pieces_Black.insert(0, (Chess_Piece, new_Postion_Col + new_Postion_Row))
        self.numberOfMoves += 1

    

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


