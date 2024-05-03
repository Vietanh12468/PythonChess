class HistoryMoves:
    def __init__(self):
        self.moves = []
        self.previousPosition = []
        self.indexPreviousMove = -1

    # previousChessPiece is the chess piece that was at the new position at the previousPosition is the position of the current chess piece move
    # for example if Qxe4, previousChessPiece is the piece that was capture by Q and previousPosition is the previous position of Q
    # More detail example, previousChessPiece = white pawn, previousPosition is the Q posion = 'e7', and Qxe4 will succesfully capture and move to 'e4'
    def Add(self, move, previousPosition, previousChessPiece):
        self.moves.insert(0, [move, previousPosition, previousChessPiece])

    def PreviousMoveInfo(self):
        if self.moves is not None:
            self.indexPreviousMove += 1
            return [self.moves[self.indexPreviousMove], len(self.moves) - self.indexPreviousMove]
        elif self.moves is None:
            print("There is no move to undo")
            return None
        else:
            print("Unknown error")
    def __str__(self):
        listMove = []
        for move in self.moves:
            listMove.insert(0, move[0])
        return str(listMove)
    def MakeNewMove(self):
        self.moves = self.moves[self.indexPreviousMove:]

