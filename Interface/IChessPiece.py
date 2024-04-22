from abc import ABC, abstractmethod
from STATIC_VARIBLE import *
from TransformPosition import *

transformer= TransormPostion()

class IchessPiece(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Move(self):
        pass

    def get_available_moves(self):
        pass

class IKing(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "King"
        self.short_name = "K"
        self.posible_Moves_Row_And_Column = [-1, 0, 1]

    # def Move(self, current_position, new_Position):
    #     current_Row, current_Column = current_position[:2]
    #     new_Row, new_Column = new_Position[:2]
    #     if int(new_Row) in ROWS and new_Column in COLUMNS and not (new_Row == current_Row and new_Column == current_Column):
    #         if int(current_Row) - int(new_Row) in self.posible_Moves_Row_And_Column and ord(current_Column.lower()) - ord(new_Column.lower()) in self.posible_Moves_Row_And_Column:
    #             return True
    #     return False
    
    def Move(self, current_position, new_Column, new_Row):
        current_Column, current_Row = current_position[:2]
        if int(new_Row) in ROWS and new_Column in COLUMNS and not (new_Row == current_Row and new_Column == current_Column):
            if int(current_Row) - int(new_Row) in self.posible_Moves_Row_And_Column and ord(current_Column.lower()) - ord(new_Column.lower()) in self.posible_Moves_Row_And_Column:
                return True
        return False

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        for row in self.posible_Moves_Row_And_Column:
            for column in self.posible_Moves_Row_And_Column:
                if int(current_Row) + row in ROWS and chr(ord(current_Column.lower()) + column) in COLUMNS and not (row == 0 and column == 0):
                    if not isinstance(board.board[int(current_Row) + row - 1][transformer.tranformColumnToNumber(chr(ord(current_Column.lower()) + column))].chess_piece, self.ally_Color):
                        list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
        return list_Of_Available_Moves
    
class IQueen(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Queen"
        self.short_name = "Q"

    def Move(self, current_position, new_Position):
        pass

    def get_available_moves(self, current_position):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        for row in ROWS:
            for column in COLUMNS:
                if row == 0 and column == 0:
                    pass
                elif current_Column == column:
                    list_Of_Available_Moves.append(f"{current_Column}{str(row)}")
                elif int(current_Row) == row:
                    list_Of_Available_Moves.append(f"{column}{current_Row}")
                elif abs(int(current_Row) - row) == abs(ord(current_Column.lower()) - ord(column.lower())):
                    list_Of_Available_Moves.append(f"{column}{str(row)}")
        return list_Of_Available_Moves
    
class IPawn(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Pawn"
        self.short_name = "P"

    def Move(self, current_position, new_Position):
        pass

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        if int(current_Row) == 2:
            list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 1)}")
            list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 2)}")
        elif board.board[int(current_Row) + 1][ord(current_Column.lower()) - 97].chess_piece == None:
            list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + 1)}")
        if isinstance(board.board[int(current_Row) - 1 + 1][ord(current_Column.lower()) - 97 - 1].chess_piece, self.opponent_Color):
            list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) - 1)}{str(int(current_Row) + 1)}")
        if isinstance(board.board[int(current_Row) - 1 + 1][ord(current_Column.lower()) - 97 + 1].chess_piece, self.opponent_Color):
            list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + 1)}{str(int(current_Row) + 1)}")
        return list_Of_Available_Moves