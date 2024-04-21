class Position:
    def __init__(self, column, row, chess_piece):
        self.column = column
        self.row = row
        self.chess_piece = chess_piece
        self.indexColumn = ord(column.lower())-97
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