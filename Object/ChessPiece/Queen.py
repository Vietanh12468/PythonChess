from Interface import *
from GlobalClass import *

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
    
class BlackQueen(IQueen, Black):
    def __init__(self):
        IQueen.__init__(self)
        Black.__init__(self)
        self.symbol = "♕ "

class WhiteQueen(IQueen, White):
    def __init__(self):
        IQueen.__init__(self)
        White.__init__(self)
        self.symbol = "♛ "