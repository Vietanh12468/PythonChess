from Interface import *
from GlobalClass import *

class IRook(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Rook"
        self.short_name = "R"

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