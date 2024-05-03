class HistoryMoves:
    def __init__(self):
        self.moves = []

    def Add(self, move):
        self.moves.append(move)

    def Undo(self):
        if not len(self.moves) == 0:
            return self.moves.pop()
        else:
            print("Cannot undo move anymore")

    def LastMove(self):
        if not len(self.moves) == 0:
            return self.moves[-1]
        else:
            print("There is no move to undo")

