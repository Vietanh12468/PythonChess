from Interface import *
from GlobalClass import *

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
            
    def ConditionToMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        return super().ConditionToMove(index_Old_Col, index_New_Row, index_New_Col, board)
    
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

class WhitePawn(IPawn, White):
    def __init__(self):
        White.__init__(self)
        IPawn.__init__(self)
        self.symbol = "♟ "
    
class BlackPawn(IPawn, Black):
    def __init__(self):
        Black.__init__(self)
        IPawn.__init__(self)
        self.symbol = "♙ "
