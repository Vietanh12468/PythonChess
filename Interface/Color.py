from abc import ABC, abstractmethod
class Icolor(ABC):
    def __init__(self):
        pass

class Black(Icolor):
    def __init__(self):
        super().__init__()
        self.symbol = "⚫"
        self.color = Black
        self.ally_Color = Black
        self.opponent_Color = White

class White(Icolor):
    def __init__(self):
        super().__init__()
        self.symbol = "⚪"
        self.color = White
        self.ally_Color = White
        self.opponent_Color = Black