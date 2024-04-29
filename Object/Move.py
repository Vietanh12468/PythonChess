from GlobalClass import VectorDirection
class Move:
    def DiagonalMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        col_Direction = VectorDirection.GetDirection(index_Old_Col, index_New_Col)
        row_Direction = VectorDirection.GetDirection(index_Old_Row, index_New_Row)
        if abs(index_New_Row - index_Old_Row) == abs(index_New_Col - index_Old_Col):
            for i in range(1, max(abs(index_New_Col - index_Old_Col), abs(index_New_Row - index_Old_Row)) + 1):
                if board.board[index_Old_Row + i * row_Direction][index_Old_Col + i * col_Direction].chess_piece != None:
                    return False
            return True
        return False
    
    def ColumnMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        row_Direction = VectorDirection.GetDirection(index_Old_Row, index_New_Row)
        if index_New_Col == index_Old_Col:
            for i in range(1, abs(index_New_Row - index_Old_Row) + 1):
                if board.board[index_Old_Row + i * row_Direction][index_Old_Col].chess_piece != None:
                    return False
            return True
        return False
    
    def RowMove(index_Old_Row, index_Old_Col, index_New_Row, index_New_Col, board):
        col_Direction = VectorDirection.GetDirection(index_Old_Col, index_New_Col)
        if index_New_Row == index_Old_Row:
            for i in range(1, abs(index_New_Col - index_Old_Col) + 1):
                if board.board[index_Old_Row][index_Old_Col + i * col_Direction].chess_piece != None:
                    return False
            return True
        return False