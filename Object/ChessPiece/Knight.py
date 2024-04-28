from Interface import *
from GlobalClass import *

class IKnight(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Knight"
        self.short_name = "N"

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