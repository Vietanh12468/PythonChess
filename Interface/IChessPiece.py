from abc import ABC, abstractmethod
from STATIC_VARIBLE import *
from TransformPosition import *

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

class IKing(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "King"
        self.short_name = "K"
        self.posible_Moves_Row_And_Column = [-1, 0, 1]

    # def Move(self, current_position, new_Position):
    #     current_Row, current_Column = current_position[:2]
    #     new_Row, new_Column = new_Position[:2]
    #     if int(new_Row) in ROWS and new_Column in COLUMNS and not (new_Row == current_Row and new_Column == current_Column):
    #         if int(current_Row) - int(new_Row) in self.posible_Moves_Row_And_Column and ord(current_Column.lower()) - ord(new_Column.lower()) in self.posible_Moves_Row_And_Column:
    #             return True
    #     return False
    
    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if board.board[index_New_Row][index_New_Col].chess_piece == None:
                    return True
        return False

    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row -index_Old_Row in self.posible_Moves_Row_And_Column and index_New_Col - index_Old_Col in self.posible_Moves_Row_And_Column:
                if isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
                    return True
        return False  

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = TransformPostion.transformColumnToNumber(current_Column)
        for row in self.posible_Moves_Row_And_Column:
            for column in self.posible_Moves_Row_And_Column:
                if int(current_Row) + row in ROWS and chr(ord(current_Column.lower()) + column) in COLUMNS and not (row == 0 and column == 0):
                    if board.board[index_Current_Row + row][index_Current_Col + column].chess_piece == None:
                        list_Of_Available_Moves.append(f"{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
                    elif isinstance(board.board[index_Current_Row + row][index_Current_Col + column].chess_piece, self.opponent_Color):
                        list_Of_Available_Moves.append(f"Kx{chr(ord(current_Column.lower()) + column)}{str(int(current_Row) + row)}")
        return list_Of_Available_Moves
    
class IQueen(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Queen"
        self.short_name = "Q"

    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if (new_Postion_Row == old_Row and new_Postion_Col == old_Col) or not (index_New_Row == index_Old_Row or index_New_Col == index_Old_Col or abs(index_New_Row - index_Old_Row) == abs(index_New_Col - index_Old_Col)):
            return False
        col_Direction = VectorDirection.GetDirection(index_Old_Col, index_New_Col)
        row_Direction = VectorDirection.GetDirection(index_Old_Row, index_New_Row)
        if index_New_Row == index_Old_Row or index_New_Col == index_Old_Col or abs(index_New_Row - index_Old_Row) == abs(index_New_Col - index_Old_Col):
            for i in range(1, max(abs(index_New_Col - index_Old_Col), abs(index_New_Row - index_Old_Row)) + 1):
                if board.board[index_Old_Row + i * row_Direction][index_Old_Col + i * col_Direction].chess_piece != None:
                    return False
            return True
        return False
    
    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board):       
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if (new_Postion_Row == old_Row and new_Postion_Col == old_Col) or not (index_New_Row == index_Old_Row or index_New_Col == index_Old_Col or abs(index_New_Row - index_Old_Row) == abs(index_New_Col - index_Old_Col)):
            return False
        col_Direction = VectorDirection.GetDirection(index_Old_Col, index_New_Col)
        row_Direction = VectorDirection.GetDirection(index_Old_Row, index_New_Row)
        if index_New_Row == index_Old_Row or index_New_Col == index_Old_Col or abs(index_New_Row - index_Old_Row) == abs(index_New_Col - index_Old_Col):
            vectorRange = max(abs(index_New_Col - index_Old_Col), abs(index_New_Row - index_Old_Row))
            for i in range(1, vectorRange + 1):
                if isinstance(board.board[index_Old_Row + i * row_Direction][index_Old_Col + i * col_Direction].chess_piece, self.opponent_Color) and i == vectorRange:
                    return True
                elif board.board[index_Old_Row + i * row_Direction][index_Old_Col + i * col_Direction].chess_piece != None:
                    return False
        return False

    def get_available_moves(self, current_position, board):
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = TransformPostion.transformColumnToNumber(current_Column)
        for vector in [1, 0, -1]:
            for vector2 in [1, 0, -1]:
                index_Next_Row = index_Current_Row + vector
                index_Next_Col = index_Current_Col + vector2
                if vector == 0 and vector2 == 0:
                    continue
                else:
                    while index_Next_Row + 1 in ROWS and TransformPostion.transformNumberToColumn(index_Next_Col) in COLUMNS:
                        next_Row = str(index_Next_Row + 1)
                        next_Col = TransformPostion.transformNumberToColumn(index_Next_Col)
                        if board.board[index_Next_Row][index_Next_Col].chess_piece == None:
                            list_Of_Available_Moves.append(f"{next_Col}{next_Row}")
                        elif isinstance(board.board[index_Next_Row][index_Next_Col].chess_piece, self.opponent_Color):
                            list_Of_Available_Moves.append(f"Qx{next_Col}{next_Row}")
                            break
                        else:
                            break
                        index_Next_Row += vector
                        index_Next_Col += vector2
        return list_Of_Available_Moves

    
class IPawn(IchessPiece):
    def __init__(self):
        super().__init__()
        self.name = "Pawn"
        self.short_name = "P"
        self.valid_Promote = ['Q', 'R', 'B', 'N']
        self.SwitchColor()

    def SwitchColor(self):
        if self.color == "White":
            self.forward = 1
            self.begin = 1
            self.maxJump = 3
            self.beforePromote = 6
        elif self.color == "Black":
            self.forward = -1
            self.begin = 6
            self.maxJump = 4
            self.beforePromote = 1


    def Move(self, current_position, new_Postion_Col, new_Postion_Row, board):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if index_New_Row == 7 or index_New_Row == 0:
            return False
        elif int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Col == index_Old_Col:
                if board.board[index_Old_Row + self.forward][index_Old_Col].chess_piece == None:
                    if index_New_Row - index_Old_Row == self.forward:
                        return True
                    elif index_Old_Row == self.begin and index_New_Row == self.maxJump and board.board[index_New_Row][index_New_Col].chess_piece == None:
                        return True
        return False
    
    def Capture(self, current_position, new_Postion_Col, new_Postion_Row, board, piece_Moved_Column):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if index_New_Row == 7 or index_New_Row == 0:
            return False
        if int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Row - index_Old_Row == self.forward and abs(index_New_Col - index_Old_Col) == 1 and isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color) and piece_Moved_Column == old_Col:
                return True
        return False

    def Promote(self, current_position, new_Postion_Col, new_Postion_Row, board, promote_Piece):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if index_Old_Row != self.beforePromote or index_New_Row != self.beforePromote + self.forward:
            return False
        elif int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if index_New_Col == index_Old_Col:
                if index_New_Row - index_Old_Row == self.forward and board.board[index_New_Row][index_New_Col].chess_piece == None:
                    if promote_Piece in self.valid_Promote:
                        return True
        return False
    
    def CapturePromote(self, current_position, new_Postion_Col, new_Postion_Row, board, promote_Piece):
        old_Col, old_Row = current_position[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        if index_Old_Row != self.beforePromote or index_New_Row != self.beforePromote + self.forward:
            return False
        elif int(new_Postion_Row) in ROWS and new_Postion_Col in COLUMNS and not (new_Postion_Row == old_Row and new_Postion_Col == old_Col):
            if abs(index_New_Col - index_Old_Col) == 1:
                if index_New_Row - index_Old_Row == self.forward and isinstance(board.board[index_New_Row][index_New_Col].chess_piece, self.opponent_Color):
                    if promote_Piece in self.valid_Promote:
                        return True
        return False

    def get_available_moves(self, current_position, board): 
        list_Of_Available_Moves = []
        current_Column, current_Row = current_position[:2]
        index_Current_Row = int(current_Row) - 1
        index_Current_Col = TransformPostion.transformColumnToNumber(current_Column)
        if board.board[index_Current_Row + self.forward][index_Current_Col].chess_piece == None:
            if index_Current_Row == self.beforePromote:
                list_Of_Available_Moves.append(f"{current_Column}{self.beforePromote+self.forward+1}=?")
            else:
                list_Of_Available_Moves.append(f"{current_Column}{str(int(current_Row) + self.forward)}")
                if index_Current_Row == self.begin and board.board[self.maxJump][index_Current_Col].chess_piece == None:
                    list_Of_Available_Moves.append(f"{current_Column}{self.maxJump+1}")

        for col_Offset in [-1, 1]:
            neighbor_Col = index_Current_Col + col_Offset
            if 0 <= neighbor_Col <= 7:
                if isinstance(board.board[index_Current_Row + self.forward][neighbor_Col].chess_piece, self.opponent_Color):
                    if index_Current_Row == self.beforePromote:
                        list_Of_Available_Moves.append(f"{current_Column}x{chr(ord(current_Column.lower()) + col_Offset)}{self.beforePromote+self.forward+1}=?")
                    else:
                        list_Of_Available_Moves.append(f"{current_Column}x{chr(ord(current_Column.lower()) + col_Offset)}{index_Current_Row + 1 + self.forward}")

        return list_Of_Available_Moves
    
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
        