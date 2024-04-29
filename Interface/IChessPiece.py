from abc import ABC, abstractmethod
from GlobalClass import *

class IchessPiece(ABC):
    def __init__(self):
        pass

    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if new_Postion_Row == old_Row and new_Postion_Col == old_Col:
            return False
        if self.ConditionToMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False

    @abstractmethod
    def get_available_moves(self):
        pass

    def ConditionToMove(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        pass

    def ConditionBeforeCapture(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        pass

    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if new_Postion_Row == old_Row and new_Postion_Col == old_Col:
            return False
        if not self.ConditionBeforeCapture(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return False
        col_Direction = VectorDirection.GetDirection(index_Old_Col, index_New_Col)
        row_Direction = VectorDirection.GetDirection(index_Old_Row, index_New_Row)
        if self.ConditionToMove(index_Old_Row, index_Old_Col, index_New_Row - row_Direction, index_New_Col - col_Direction, board):
            if isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
                return True
        return False
            

        