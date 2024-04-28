class TransformPostion:
    def transformColumnToNumber(column):
        return ord(column.lower())-97

    def transformNumberToColumn(number):
        return chr(number + 97)