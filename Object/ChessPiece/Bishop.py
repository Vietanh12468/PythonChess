from Interface import *
from GlobalClass import *

class IBishop(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Bishop"
        self.short_name = "B"

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