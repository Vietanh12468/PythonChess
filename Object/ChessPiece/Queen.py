from Interface import *
from GlobalClass import *
from Object.Move import *

class IQueen(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Queen"
        self.short_name = "Q"

    def ConditionBeforeCapture(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if index_Old_Row == index_New_Row or index_Old_Col == index_New_Col or abs(index_Old_Row - index_New_Row) == abs(index_Old_Col - index_New_Col):
            return True
        return False

    def ConditionToMove(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if Move.DiagonalMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        elif Move.ColumnMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        elif Move.RowMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = TransformPostion.transformColumnToNumber(current_Column)
        for vector in [1, 0, -1]:
            for vector2 in [1, 0, -1]:
                index_Next_Row = index_Current_Row + vector
                index_Next_Col = index_Current_Col + vector2
                if vector == 0 and vector2 == 0:
                    continue
                else:
                    while index_Next_Row + 1 in ROWS and TransformPostion.transformNumberToColumn(index_Next_Col) in COLUMNS:
                        next_Row = str(index_Next_Row + 1)
                        next_Col = TransformPostion.transformNumberToColumn(index_Next_Col)
                        if board.board[index_Next_Row][index_Next_Col].chess_piece == None:
                            list_Of_Available_Moves.append(f"{next_Col}{next_Row}")
                        elif isinstance(board.board[index_Next_Row][index_Next_Col].chess_piece, self.opponent_Color):
                            list_Of_Available_Moves.append(f"Qx{next_Col}{next_Row}")
                            break
                        else:
                            break
                        index_Next_Row += vector
                        index_Next_Col += vector2
        return list_Of_Available_Moves
    
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