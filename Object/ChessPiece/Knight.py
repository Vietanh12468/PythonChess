from Interface import *
from GlobalClass import *
from Object.Move import *

class IKnight(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Knight"
        self.short_name = "N"

    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if new_Postion_Row == old_Row and new_Postion_Col == old_Col:
            return False
        if self.ConditionBeforeCapture(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False
    
    def ConditionBeforeCapture(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if Move.KnightCapture(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False

    def ConditionToMove(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if Move.KnightMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False

    def get_available_moves(self):
        pass
    
class BlackKnight(IKnight, Black):
    def __init__(self):
        IKnight.__init__(self)
        Black.__init__(self)
        self.symbol = "♘ "

class WhiteKnight(IKnight, White):
    def __init__(self):
        IKnight.__init__(self)
        White.__init__(self)
        self.symbol = "♞ "