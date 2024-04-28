from abc import ABC, abstractmethod

class IchessPiece(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Move(self):
        pass

    def get_available_moves(self):
        pass

    def Capture(self):
        pass
    
class VectorDirection:
    def GetDirection(current_Vector, new_Vector):
        if current_Vector > new_Vector:
            return -1
        elif current_Vector < new_Vector:
            return 1
        elif current_Vector == new_Vector:
            return 0
        else:
            raise Exception("Unknown Error")
        