from Interface import *
from GlobalClass import *

class IKing(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "King"
        self.short_name = "K"
        self.posible_Moves_Row_And_Column = [-1, 0, 1]
    
    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if board.board[index_New_Row][index_New_Col].chess_piece == None:
                    return True
        return False

    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
                    return True
        return False  

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = TransformPostion.transformColumnToNumber(current_Column)
        for row in self.posible_Moves_Row_And_Column:
            for column in self.posible_Moves_Row_And_Column:
                if int(current_Row) + row in ROWS and chr(ord(current_Column.lower()) + column) in COLUMNS and not (row == 0 and column == 0):
                    if board.board[index_Current_Row + row][index_Current_Col + column].chess_piece == None:
                        list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
                    elif isinstance(board.board[index_Current_Row + row][index_Current_Col + column].chess_piece, self.opponent_Color):
                        list_Of_Available_Moves.append(f"Kx{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
        return list_Of_Available_Moves
    
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
