import ChessPython

new_board = ChessPython.Board()

blackKing = ChessPython.BlackKing()
blackQueen = ChessPython.BlackQueen()
whiteQueen = ChessPython.WhiteQueen()
whitePawn = ChessPython.WhitePawn()
blackPawn = ChessPython.BlackPawn()
new_board.addChessPiece(blackKing, "a8")
new_board.addChessPiece(whiteQueen, "h1")
new_board.addChessPiece(whiteQueen, "a7")
new_board.addChessPiece(blackQueen, "b7")
new_board.addChessPiece(whitePawn, "h2")
new_board.addChessPiece(whitePawn, "a3")
new_board.addChessPiece(whitePawn, "b3")
new_board.addChessPiece(blackPawn, "c4")
new_game = ChessPython.Game(new_board)

# print the board
for row in new_board.board:
    for position in row:
        print(position.tostring(), end=" ")
    print(",")

new_board.printBoard()

new_game.MoveChessPiece("Kb8")
new_game.MoveChessPiece("a4")
# new_game.MoveChessPiece("Qd1")
new_game.board.printBoard()

print("Info:", new_game.ShowChessPieceInfo("b3"))