from Object.Position import *
from STATIC_VARIBLE import *

class Board:
    def __init__(self):
        # perform creation of board
        self.board = [[Position(col, row, None) for col in COLUMNS] for row in ROWS]

    def findPosition(self, position):
        
        # check if the position is a string and the length is = 2
        if type(position) == str and len(position) == 2:
            # perform split the string
            p1, p2 = position[:2]
            # check if the position is valid
            if p1 in COLUMNS and int(p2) in ROWS:
                i = 0
                while i < len(COLUMNS):
                    if self.board[int(p2)-1][i].tostring() == position:
                        return self.board[int(p2)-1][i]
                    i += 1
            elif p2 in COLUMNS and int(p1) in ROWS:
                i = 0
                while i < len(COLUMNS):
                    if self.board[int(p1)-1][i].tostring() == position:
                        return self.board[int(p1)-1][i]
                    i += 1
            else:
                return None
            
    # def findChessPiece(self, chess_piece, position):
    #     positionInBoard = self.findPosition(position)

    def addChessPiece(self, chess_piece, position):
        positionInBoard = self.findPosition(position)
        if positionInBoard != None:
            positionInBoard.SetChessPiece(chess_piece)
            return f"{chess_piece} has been added into {position}"
        else:
            return f"{position} is not a valid position"

    def printBoard(self):
        start_Row = 1
        for row in self.board:
            print(start_Row, end="")
            for position in row:
                print(position.toPiece(), end=" ")
            print("")
            start_Row += 1
        print("  ", end="")
        for col in COLUMNS:
            print(col + " ", end=" ")
        print("")
