from Interface import *
from GlobalClass import *
from Object.Move import *

class IRook(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Rook"
        self.short_name = "R"
    def ConditionBeforeCapture(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if index_New_Col == index_Old_Col or index_New_Row == index_Old_Row:
            return True
        return False

    def ConditionToMove(self, index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        if Move.RowMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board) or Move.ColumnMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
            return True
        return False
    
    def get_available_moves(self):
        pass
    
class BlackRook(IRook, Black):
    def __init__(self):
        IRook.__init__(self)
        Black.__init__(self)
        self.symbol = "♖ "

class WhiteRook(IRook, White):
    def __init__(self):
        IRook.__init__(self)
        White.__init__(self)
        self.symbol = "♜ "