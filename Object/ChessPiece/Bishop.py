from Interface import *
from GlobalClass import *
from Object.Move import *

class IBishop(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Bishop"
        self.short_name = "B"

    def ConditionBeforeCapture(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if abs(index_Old_Row - index_New_Row) == abs(index_Old_Col - index_New_Col):
            return True
        return False

    def ConditionToMove(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if Move.DiagonalMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False
    
    def get_available_moves(self):
        pass

class BlackBishop(IBishop, Black):
    def __init__(self):
        IBishop.__init__(self)
        Black.__init__(self)
        self.symbol = "♗ "

class WhiteBishop(IBishop, White):
    def __init__(self):
        IBishop.__init__(self)
        White.__init__(self)
        self.symbol = "♝ "