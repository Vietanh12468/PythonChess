import ChessPython

new_board = ChessPython.Board()
history = ChessPython.HistoryMoves()

new_board.addChessPiece(ChessPython.BlackRook(), "a8")
new_board.addChessPiece(ChessPython.BlackRook(), "h8")
new_board.addChessPiece(ChessPython.WhiteRook(), "a1")
new_board.addChessPiece(ChessPython.WhiteRook(), "h1")
new_board.addChessPiece(ChessPython.BlackKnight(), "b8")
new_board.addChessPiece(ChessPython.BlackKnight(), "g8")
new_board.addChessPiece(ChessPython.WhiteKnight(), "b1")
new_board.addChessPiece(ChessPython.WhiteKnight(), "g1")
new_board.addChessPiece(ChessPython.BlackBishop(), "c8")
new_board.addChessPiece(ChessPython.BlackBishop(), "f8")
new_board.addChessPiece(ChessPython.WhiteBishop(), "c1")
new_board.addChessPiece(ChessPython.WhiteBishop(), "f1")
new_board.addChessPiece(ChessPython.BlackQueen(), "d8")
new_board.addChessPiece(ChessPython.WhiteQueen(), "d1")
new_board.addChessPiece(ChessPython.BlackKing(), "e8")
new_board.addChessPiece(ChessPython.WhiteKing(), "e1")

new_board.addChessPiece(ChessPython.BlackPawn(), "a7")
new_board.addChessPiece(ChessPython.BlackPawn(), "b7")
new_board.addChessPiece(ChessPython.BlackPawn(), "c7")
new_board.addChessPiece(ChessPython.BlackPawn(), "d7")
new_board.addChessPiece(ChessPython.BlackPawn(), "e7")
new_board.addChessPiece(ChessPython.BlackPawn(), "f7")
new_board.addChessPiece(ChessPython.BlackPawn(), "g7")
new_board.addChessPiece(ChessPython.BlackPawn(), "h7")

new_board.addChessPiece(ChessPython.WhitePawn(), "a2")
new_board.addChessPiece(ChessPython.WhitePawn(), "b2")
new_board.addChessPiece(ChessPython.WhitePawn(), "c2")
new_board.addChessPiece(ChessPython.WhitePawn(), "d2")
new_board.addChessPiece(ChessPython.WhitePawn(), "e2")
new_board.addChessPiece(ChessPython.WhitePawn(), "f2")
new_board.addChessPiece(ChessPython.WhitePawn(), "g2")
new_board.addChessPiece(ChessPython.WhitePawn(), "h2")

new_game = ChessPython.Game(new_board)

new_game.board.printBoard()

while True:
    user_input = input("Enter a command: ")

    if user_input == "move":
        while True:
            user_input = input("Enter a move: ")
            if new_game.MoveChessPiece(user_input):
                new_game.board.printBoard()
                history.Add(user_input)
            elif user_input == "exit":
                break

    elif user_input == "undo":
        history.Undo()
        new_game.board.printBoard()

    elif user_input == "history":
        print(history.moves)

    elif user_input == "last move":
        print(history.LastMove())
        
    elif user_input == "Help":
        print("Enter 'move' to make a move, 'undo' to undo a move, and 'exit' to quit")

    elif user_input == "exit":
        break

    else:
        print("Not a valid command")