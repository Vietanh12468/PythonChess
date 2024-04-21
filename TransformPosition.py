class TransormPostion:
    def tranformColumnToNumber(self, column):
        return ord(column.lower())-97

    def tranformNumberToColumn(self, number):
        return str(number + 97)