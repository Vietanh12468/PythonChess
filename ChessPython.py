from abc import ABC, abstractmethod

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = [1, 2, 3, 4, 5, 6, 7, 8]

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


    def move(self, position):
        Position.OnMove(self, position)


class BlackKing(IKing):
    def __init__(self):
        super().__init__()
        self.symbol = "♚"

class WhiteKing(IKing):
    def __init__(self):
        super().__init__()
        self.symbol = "♔"
    

class Position:
    def __init__(self, column, row, chess_piece):
        self.column = column
        self.row = row
        self.chess_piece = chess_piece
        self.indexColumn = ord(column.lower())-1-97
        self.indexRow = row-1

    def SetChessPiece(self, chess_piece):
        self.chess_piece = chess_piece

    def tostring(self):
        return f"{self.column}{self.row}"
    
    def toPiece(self):
        if self.chess_piece != None:
            return self.chess_piece.symbol
        else:
            if (self.indexColumn % 2 == 0 and self.indexRow % 2 == 0) or (self.indexColumn % 2 == 1 and self.indexRow % 2 == 1):
                return "⬜"
            else:
                return "⬛"

class Board:
    def __init__(self):
        # perform creation of board
        self.rows = rows
        self.columns = columns
        self.board = [[Position(col, row, None) for col in columns] for row in rows]

    def find_position(self, position):
        
        # check if the position is a string and the length is = 2
        if type(position) == str and len(position) == 2:
            # perform split the string
            p1, p2 = position[:2]
            # check if the position is valid
            if p1 in columns and int(p2) in rows:
                i = 0
                while i < len(columns)-1:
                    if self.board[int(p2)-1][i].tostring() == position:
                        return self.board[int(p2)-1][i]
                    i += 1
            elif p2 in columns and int(p1) in rows:
                i = 0
                while i < len(columns)-1:
                    if self.board[int(p1)-1][i].tostring() == position:
                        return self.board[int(p1)-1][i]
                    i += 1
            else:
                return None

    def add_piece(self, chess_piece, position):
        positionInBoard = self.find_position(position)
        if positionInBoard != None:
            positionInBoard.SetChessPiece(chess_piece)
            return f"{chess_piece} has been added into {position}"
        else:
            return f"{position} is not a valid position"

    def print_board(self):
        for row in self.board:
            for position in row:
                print(position.toPiece(), end=" ")
            print(",")

        
class Game:
    def __init__(self):
        self.board = Board()

    # def generate_chess_pieces(self):
    #     for col in range(8):


