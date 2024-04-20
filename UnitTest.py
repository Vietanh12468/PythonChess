import ChessPython

# create a new board
new_board = ChessPython.Board()

# print the board
for row in new_board.board:
    for position in row:
        print(position.tostring(), end=" ")
    print(",")

blackKing = ChessPython.BlackKing()
new_board.add_piece(blackKing, "a8")

new_board.print_board()