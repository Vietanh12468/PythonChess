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
    
    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = transformer.tranformColumnToNumber(old_Col)
        index_New_Col = transformer.tranformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if board.board[index_New_Row][index_New_Col].chess_piece == None:
                    return True
        return False

    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = transformer.tranformColumnToNumber(old_Col)
        index_New_Col = transformer.tranformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
                    return True
        return False  

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = transformer.tranformColumnToNumber(current_Column)
        for row in self.posible_Moves_Row_And_Column:
            for column in self.posible_Moves_Row_And_Column:
                if int(current_Row) + row in ROWS and chr(ord(current_Column.lower()) + column) in COLUMNS and not (row == 0 and column == 0):
                    if board.board[index_Current_Row + row][index_Current_Col + column].chess_piece == None:
                        list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
                    elif isinstance(board.board[index_Current_Row + row][index_Current_Col + column].chess_piece, self.opponent_Color):
                        list_Of_Available_Moves.append(f"Kx{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
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
        self.SwitchColor()

    def SwitchColor(self):
        if self.color == "White":
            self.forward = 1
            self.begin = 1
            self.maxJump = 3
            self.beforePromote = 6
        elif self.color == "Black":
            self.forward = -1
            self.begin = 6
            self.maxJump = 4
            self.beforePromote = 1


    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = transformer.tranformColumnToNumber(old_Col)
        index_New_Col = transformer.tranformColumnToNumber(new_Postion_Col)
        if index_New_Row == 7 or index_New_Row == 0:
            return False
        elif int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Col == index_Old_Col:
                if board.board[index_Old_Row + self.forward][index_Old_Col].chess_piece == None:
                    if index_New_Row - index_Old_Row == self.forward:
                        return True
                    elif index_Old_Row == self.begin and index_New_Row == self.maxJump and board.board[index_New_Row][index_New_Col].chess_piece == None:
                        return True
            # elif index_New_Row - index_Old_Row == self.forward and abs(index_New_Col - index_Old_Col) == 1 and isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
            #     return True
        return False
    # def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
    #     old_Col, old_Row = current_position[:2]
    #     index_Old_Row = int(old_Row) - 1
    #     index_New_Row = int(new_Postion_Row) - 1
    #     index_Old_Col = transformer.tranformColumnToNumber(old_Col)
    #     index_New_Col = transformer.tranformColumnToNumber(new_Postion_Col)
    #     if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
    #         if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
    #             if isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
    #                 return True
    #     return False  
    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = transformer.tranformColumnToNumber(old_Col)
        index_New_Col = transformer.tranformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if index_New_Row - index_Old_Row == self.forward and abs(index_New_Col - index_Old_Col) == 1 and isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
                    return True
        return False
    
    def Promote(self, current_position, new_Postion_Col, new_Postion_Row, board):
        return False


    def get_available_moves(self, current_position, board): 
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = transformer.tranformColumnToNumber(current_Column)
        if board.board[index_Current_Row + self.forward][index_Current_Col].chess_piece == None:
            if index_Current_Row == self.beforePromote:
                list_Of_Available_Moves.append(f"{current_Column}{self.beforePromote+self.forward+1}=?")
            else:
                list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + self.forward)}")
                if index_Current_Row == self.begin and board.board[self.maxJump][index_Current_Col].chess_piece == None:
                    list_Of_Available_Moves.append(f"{current_Column}{self.maxJump+1}")

        if index_Current_Col - 1 >= 0:
            if isinstance(board.board[index_Current_Row + self.forward][index_Current_Col - 1].chess_piece, self.opponent_Color):
                if index_Current_Row == self.beforePromote:
                    list_Of_Available_Moves.append(f"{current_Column}x{chr(ord(current_Column.lower()) - 1)}{self.beforePromote+self.forward+1}=?")
                else:
                    list_Of_Available_Moves.append(f"{current_Column}x{chr(ord(current_Column.lower()) - 1)}{index_Current_Row + 1 + self.forward}")
        if index_Current_Col + 1 <= 7:
            if isinstance(board.board[index_Current_Row + self.forward][index_Current_Col + 1].chess_piece, self.opponent_Color):
                if index_Current_Row == self.beforePromote:
                    list_Of_Available_Moves.append(f"{current_Column}x{chr(ord(current_Column.lower()) + 1)}{self.beforePromote+self.forward+1}=?")
                else:
                    list_Of_Available_Moves.append(f"{current_Column}x{chr(ord(current_Column.lower()) + 1)}{index_Current_Row + 1 +  self.forward}")
            
        return list_Of_Available_Moves