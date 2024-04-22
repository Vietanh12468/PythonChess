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
        super().__init__()
        self.symbol = "♚ "

class BlackQueen(IQueen, Black):
    def __init__(self):
        super().__init__()
        self.symbol = "♕ "

class WhiteQueen(IQueen, White):
    def __init__(self):
        super().__init__()
        self.symbol = "♛ "

class BlackPawn(IPawn, Black):
    def __init__(self):
        super().__init__()
        self.symbol = "♙ "

class WhitePawn(IPawn, White):
    def __init__(self):
        super().__init__()
        self.symbol = "♟ "
    def get_available_moves(self, current_position):
        pass
    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        if int(current_Row) == 2:
            list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 1)}")
            list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 2)}")
        elif board.board[int(current_Row) + 1][ord(current_Column.lower()) - 97].chess_piece == None:
            list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 1)}")
            if isinstance(board.board[int(current_Row) + 1][ord(current_Column.lower()) - 97 - 1].chess_piece, Black):
                list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) - 1)}{str(int(current_Row) + 1)}")
            if isinstance(board.board[int(current_Row) + 1][ord(current_Column.lower()) - 97 + 1].chess_piece, Black):
                list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + 1)}{str(int(current_Row) + 1)}")
        return list_Of_Available_Moves

        # else:
        #     list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 1)}")
        #     if isinstance(board.board[int(current_Row) + 1][ord(current_Column.lower()) - 97].chess_piece, Black):
        #         list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) - 1)}{str(int(current_Row) + 1)}")

        # return list_Of_Available_Moves

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
            if type(piece[0]) == type(chess_Piece) and isinstance(piece[0], Black):
                current_Postion = piece[1]
                break
        return chess_Piece.get_available_moves(current_Postion)
    
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
            for piece in self.list_Chess_Pieces:
                if piece[0].short_name == pie:
                    if col + ro in piece[0].get_available_moves(piece[1], self.board):
                        old_Col, old_Row = piece[1][:2]
                        self.board.board[int(old_Row) - 1][transformer.tranformColumnToNumber(old_Col)].SetChessPiece(None)
                        self.board.board[int(ro)-1][transformer.tranformColumnToNumber(col)].SetChessPiece(piece[0])
                        self.list_Chess_Pieces.insert(0, (self.board.board[int(ro)-1][transformer.tranformColumnToNumber(col)].chess_piece, self.board.board[int(ro)-1][transformer.tranformColumnToNumber(col)].tostring()))
                        self.list_Chess_Pieces.remove(piece) 
                        return True
        print("Invalid move")
        return False
    



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


