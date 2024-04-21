from abc import ABC, abstractmethod
from STATIC_VARIBLE import *

class IchessPiece(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def move(self, position):
        pass

    def get_available_moves(self):
        pass

class IKing(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "King"
        self.short_name = "k"
        self.posible_Moves_Row_And_Column = [-1, 0, 1]


    def move(self, current_position, new_Position):
        current_Row, current_Column = current_position[:2]
        new_Row, new_Column = new_Position[:2]
        # if int(current_Row) - int(new_Row) in posible_Moves_Row_And_Column and ord(current_Column.lower()) - ord(new_Column.lower()) in posible_Moves_Row_And_Column:
        #     return []

    def get_available_moves(self, current_position):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        for row in self.posible_Moves_Row_And_Column:
            for column in self.posible_Moves_Row_And_Column:
                if int(current_Row) + row in ROWS and chr(ord(current_Column.lower()) + column) in COLUMNS and not (row == 0 and column == 0):
                    list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
        return list_Of_Available_Moves