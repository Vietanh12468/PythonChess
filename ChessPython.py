# from Interface.IChessPiece import *
# from Interface.Color import *
# from TransformPosition import *
# from STATIC_VARIBLE import *
# from Object.Board import *
# from Object.Position import *
# from Object.King import *
from Interface import *
from Object import *
from GlobalClass import *

class Game:
    def __init__(self, board):
        self.board = board
        self.list_Chess_Pieces_White = []
        self.list_Chess_Pieces_Black = []
        self.numberOfMoves = 0
        i = 0
        while i < 8:
            n = 0
            while n < 8:
                this_Chess_Piece = self.board.board[i][n].chess_piece
                this_Position = self.board.board[i][n].tostring()
                if this_Chess_Piece == None:
                    pass
                elif isinstance(this_Chess_Piece, IchessPiece) and isinstance(this_Chess_Piece, White):
                    self.list_Chess_Pieces_White.append((this_Chess_Piece, this_Position))
                elif isinstance(this_Chess_Piece, IchessPiece) and isinstance(this_Chess_Piece, Black):
                    self.list_Chess_Pieces_Black.append((this_Chess_Piece, this_Position))
                n += 1
            i += 1

    def all_List_Chess_Pieces(self):
        return self.list_Chess_Pieces_White + self.list_Chess_Pieces_Black

    def current_Turn(self):
        if self.numberOfMoves % 2 == 0:
            return "White"
        else:
            return "Black"
    
    def ShowAvailableMoves(self, Postion):
        for piece in self.all_List_Chess_Pieces():
            if piece[1] == Postion:
                return piece[0].get_available_moves(piece[1], self.board)
    
    def ShowChessPieceInfo(self, Postion):
        for piece in self.all_List_Chess_Pieces():
            if piece[1] == Postion:
                return piece[1] + ": " + piece[0].color + " " + piece[0].name + ", available moves: " + str(piece[0].get_available_moves(piece[1], self.board))
    
    # Fixing and Adding Required
    def MoveChessPiece(self, move_Code):
        if not 2 <= len(move_Code) <= 6:
            print("Too much or too few information in move code")
            return False

        if move_Code[0] not in COLUMNS and move_Code[0] not in PIECES:
            print("Invalid move code syntax, first character not a column or piece name")
            return False
        
        if self.current_Turn() == "White":
            this_Turn_Chess_Pieces_List = self.list_Chess_Pieces_White
        else:
            this_Turn_Chess_Pieces_List = self.list_Chess_Pieces_Black

        piece_Index = 0
        move_Piece = None
        move_Piece_Position = None
        i = 0

        if len(move_Code) == 2:
            col, ro = move_Code[:2]
            if CheckValidColAndRow.Switch(col, ro) == False:
                print("Invalid move code syntax")
                return False
            for piece in this_Turn_Chess_Pieces_List:
                if isinstance(piece[0], IPawn):
                    if piece[0].Move(piece[1], col, ro, self.board):
                        piece_Index = i
                        move_Piece = piece[0]
                        move_Piece_Position = piece[1]
                        self.UpdateBoardAfterMove(move_Piece, move_Piece_Position, col, ro, piece_Index)
                        return True
                i += 1
            print("Invalid move, Cannot move that piece or piece does not exist")
            return False
                    
        elif len(move_Code) == 3:
            pie, col, ro = move_Code[:3]
            if CheckValidColAndRow.Switch(col, ro) == False:
                print("Invalid move code syntax")
                return False
            pie_Type = PieceSwitch().Switch(pie)
            for piece in this_Turn_Chess_Pieces_List:
                if isinstance(piece[0], pie_Type):
                    if piece[0].Move(piece[1], col, ro, self.board):
                        if move_Piece == None:
                            piece_Index = i
                            move_Piece = piece[0]
                            move_Piece_Position = piece[1]
                        elif move_Piece != None:
                            print ("Invalid move, Unclear what pawn to move")
                            return False
                i += 1
            if move_Piece != None:
                self.UpdateBoardAfterMove(move_Piece, move_Piece_Position, col, ro, piece_Index)
                return True
            else:
                print("Invalid move, Cannot move that piece or piece does not exist")
                return False
        
        elif len(move_Code) == 4:
            pie = move_Code[0]
            pie_Type = PieceSwitch().Switch(pie)
            if pie in PIECES:
                addition_Info, col, ro = move_Code[1:4]
                if addition_Info != 'x' and addition_Info not in ROWS:
                    print("Invalid move code syntax, not an action can perform")
                    return False
                if CheckValidColAndRow.Switch(col, ro) == False:
                    print("Invalid move code syntax")
                    return False
                
                if addition_Info == "x":
                    for piece in this_Turn_Chess_Pieces_List:
                        if isinstance(piece[0], pie_Type):
                            if piece[0].Capture(piece[1], col, ro, self.board):
                                if move_Piece == None:
                                    piece_Index = i
                                    move_Piece = piece[0]
                                    move_Piece_Position = piece[1]
                                elif move_Piece != None:
                                    print ("Invalid move, Unclear what " + piece[0].name + " to move")
                                    return False
                        i += 1
                elif addition_Info in ROWS:
                    for piece in this_Turn_Chess_Pieces_List:
                        if isinstance(piece[0], pie_Type):
                            if piece[0].Move(piece[1], col, ro, self.board, addition_Info):
                                if move_Piece == None:
                                    piece_Index = i
                                    move_Piece = piece[0]
                                    move_Piece_Position = piece[1]
                                elif move_Piece != None:
                                    print ("Invalid move, Unclear what " + piece[0].name + " to move")
                                    return False
                        i += 1
                if move_Piece != None:
                    self.UpdateBoardAfterMove(move_Piece, move_Piece_Position, col, ro, piece_Index)
                    return True
                else:
                    print("Invalid move, Cannot move that piece or piece does not exist")
                    return False
                
            elif pie in COLUMNS:
                if 'x' in move_Code[1]:
                    addition_Info, col, ro = move_Code[1:4]
                    if CheckValidColAndRow.Switch(col, ro) == False:
                        print("Invalid move code syntax")
                        return False
                    for piece in this_Turn_Chess_Pieces_List:
                        if isinstance(piece[0], pie_Type):
                            if piece[0].Capture(piece[1], col, ro, self.board, pie):
                                piece_Index = i
                                move_Piece = piece[0]
                                move_Piece_Position = piece[1]
                                self.UpdateBoardAfterCapture(move_Piece, move_Piece_Position, col, ro, piece_Index)
                                return True
                        i += 1
                    print("Invalid move, Cannot move that piece or piece does not exist")
                    return False
                            
                elif '=' in move_Code[2]:
                    col, ro, addition_Info, promote_Pie = move_Code[:4]
                    if CheckValidColAndRow.Switch(col, ro) == False:
                        print("Invalid move code syntax")
                        return False
                    for piece in this_Turn_Chess_Pieces_List:
                        if isinstance(piece[0], pie_Type):
                            if piece[0].Promote(piece[1], col, ro, self.board, promote_Pie):
                                piece_Index = i
                                move_Piece = piece[0]
                                move_Piece_Position = piece[1]
                                self.UpdateBoardAfterPromote(promote_Pie, move_Piece_Position, col, ro, piece_Index)
                                return True
                        i += 1
                    print("Invalid move, Cannot move that piece or piece does not exist")
                    return False
                
                print("Invalid move code syntax, not an action can perform")
                return False
            
        elif len(move_Code) == 5:
            pie, addition_Info, action, col, ro = move_Code[0:5]
            if action != 'x' or not ((isinstance(addition_Info, int) and addition_Info in ROWS) or (addition_Info in COLUMNS)) or not CheckValidColAndRow.Switch(col, ro):
                print("Invalid move code syntax")
                return False
            pie_Type = PieceSwitch().Switch(pie)
            for piece in this_Turn_Chess_Pieces_List:
                if isinstance(piece[0], pie_Type) and addition_Info in piece[1]:
                    if piece[0].Capture(piece[1], col, ro, self.board):
                        piece_Index = i
                        move_Piece = piece[0]
                        move_Piece_Position = piece[1]
                        self.UpdateBoardAfterCapture(move_Piece, move_Piece_Position, col, ro, piece_Index)
                        return True
                    i += 1
            print("Invalid move, Cannot move that piece or piece does not exist")
            return False

        elif len(move_Code) == 6 and '=' in move_Code:
            current_Col, action1, col, ro, action2, promote_Pie = move_Code
            if action1 != 'x' or action2 != '=' or not CheckValidColAndRow.Switch(col, ro):
                print("Invalid move code syntax")
                return False

            for piece in this_Turn_Chess_Pieces_List:
                if isinstance(piece[0], IPawn) and current_Col == piece[1][0]:
                    if piece[0].CapturePromote(piece[1], col, ro, self.board, promote_Pie):
                        piece_Index = i
                        move_Piece = piece[0]
                        move_Piece_Position = piece[1]
                        self.UpdateBoardAfterCapturePromote(promote_Pie, move_Piece_Position, col, ro, piece_Index)
                        return True
                i += 1
            print("Invalid move, Cannot move that piece or piece does not exist")
            return False

        print("Invalid move code syntax, Unknow error")
        return False
    
    def UpdateBoardAfterMove(self, Chess_Piece, old_Postion, new_Postion_Col, new_Postion_Row, piece_Index):
        old_Col, old_Row = old_Postion[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        self.board.board[index_Old_Row][index_Old_Col].SetChessPiece(None)
        self.board.board[index_New_Row][index_New_Col].SetChessPiece(Chess_Piece)
        if self.current_Turn() == "White":
            self.list_Chess_Pieces_White.pop(piece_Index)
            self.list_Chess_Pieces_White.insert(0, (Chess_Piece, new_Postion_Col + new_Postion_Row))
        else:
            self.list_Chess_Pieces_Black.pop(piece_Index)
            self.list_Chess_Pieces_Black.insert(0, (Chess_Piece, new_Postion_Col + new_Postion_Row))
        self.numberOfMoves += 1

    def UpdateBoardAfterCapture(self, Chess_Piece, old_Postion, new_Postion_Col, new_Postion_Row, piece_Index):
        old_Col, old_Row = old_Postion[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        self.board.board[index_Old_Row][index_Old_Col].SetChessPiece(None)
        self.board.board[index_New_Row][index_New_Col].SetChessPiece(Chess_Piece)
        if self.current_Turn() == "White":
            self.list_Chess_Pieces_White.pop(piece_Index)
            self.list_Chess_Pieces_White.insert(0, (Chess_Piece, new_Postion_Col + new_Postion_Row))
            for piece in self.list_Chess_Pieces_Black:
                if piece[1] == new_Postion_Col + new_Postion_Row:
                    self.list_Chess_Pieces_Black.remove(piece)
        else:
            self.list_Chess_Pieces_Black.pop(piece_Index)
            self.list_Chess_Pieces_Black.insert(0, (Chess_Piece, new_Postion_Col + new_Postion_Row))
            for piece in self.list_Chess_Pieces_White:
                if piece[1] == new_Postion_Col + new_Postion_Row:
                    self.list_Chess_Pieces_White.remove(piece)
        self.numberOfMoves += 1

    def UpdateBoardAfterPromote(self, piece_Promote_Short, old_Postion, new_Postion_Col, new_Postion_Row, piece_Index):
        old_Col, old_Row = old_Postion[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        self.board.board[index_Old_Row][index_Old_Col].SetChessPiece(None)
        if self.current_Turn() == "White":
            piece_Promote = PieceSwitchWhite().Switch(piece_Promote_Short)
            self.board.board[index_New_Row][index_New_Col].SetChessPiece(piece_Promote)
            self.list_Chess_Pieces_White.pop(piece_Index)
            self.list_Chess_Pieces_White.insert(0, (piece_Promote, new_Postion_Col + new_Postion_Row))
        else:
            piece_Promote = PieceSwitchBlack().Switch(piece_Promote_Short)
            self.board.board[index_New_Row][index_New_Col].SetChessPiece(piece_Promote)
            self.list_Chess_Pieces_Black.pop(piece_Index)
            self.list_Chess_Pieces_Black.insert(0, (piece_Promote, new_Postion_Col + new_Postion_Row))
        self.numberOfMoves += 1

    def UpdateBoardAfterCapturePromote(self, piece_Promote_Short, old_Postion, new_Postion_Col, new_Postion_Row, piece_Index):
        old_Col, old_Row = old_Postion[:2]
        index_Old_Row = int(old_Row) - 1
        index_New_Row = int(new_Postion_Row) - 1
        index_Old_Col = TransformPostion.transformColumnToNumber(old_Col)
        index_New_Col = TransformPostion.transformColumnToNumber(new_Postion_Col)
        self.board.board[index_Old_Row][index_Old_Col].SetChessPiece(None)
        if self.current_Turn() == "White":
            piece_Promote = PieceSwitchWhite().Switch(piece_Promote_Short)
            self.board.board[index_New_Row][index_New_Col].SetChessPiece(piece_Promote)
            self.list_Chess_Pieces_White.pop(piece_Index)
            self.list_Chess_Pieces_White.insert(0, (piece_Promote, new_Postion_Col + new_Postion_Row))
            for piece in self.list_Chess_Pieces_Black:
                if piece[1] == new_Postion_Col + new_Postion_Row:
                    self.list_Chess_Pieces_Black.remove(piece)
        else:
            piece_Promote = PieceSwitchBlack().Switch(piece_Promote_Short)
            self.board.board[index_New_Row][index_New_Col].SetChessPiece(piece_Promote)
            self.list_Chess_Pieces_Black.pop(piece_Index)
            self.list_Chess_Pieces_Black.insert(0, (piece_Promote, new_Postion_Col + new_Postion_Row))
            for piece in self.list_Chess_Pieces_White:
                if piece[1] == new_Postion_Col + new_Postion_Row:
                    self.list_Chess_Pieces_White.remove(piece)
        self.numberOfMoves += 1

class CheckValidColAndRow:
    def Switch(col, row):
        try:
            if col in COLUMNS and int(row) in ROWS:
                return True
            else:
                return False
        except ValueError:
            return False
  
class PieceSwitch:
    def Switch(self, pie):
        match pie:
            case "K" :
                return IKing
            case "Q" :
                return IQueen
            case "R" :
                return IRook
            case "B" :
                return IBishop
            case "N" :
                return IKnight
            case _:
                return IPawn
            
class PieceSwitchWhite(PieceSwitch):
    def Switch(self, pie):
        match pie:
            case "K" :
                return WhiteKing()
            case "Q" :
                return WhiteQueen()
            case "R" :
                return WhiteRook()
            case "B" :
                return WhiteBishop()
            case "N" :
                return WhiteKnight()
            case _:
                return WhitePawn()
            
class PieceSwitchBlack(PieceSwitch):
    def Switch(self, pie):
        match pie:
            case "K" :
                return BlackKing()
            case "Q" :
                return BlackQueen()
            case "R" :
                return BlackRook()
            case "B" :
                return BlackBishop()
            case "N" :
                return BlackKnight()
            case _:
                return BlackPawn()