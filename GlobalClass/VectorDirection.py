class VectorDirection:
    def GetDirection(current_Vector, new_Vector):
        if current_Vector > new_Vector:
            return -1
        elif current_Vector < new_Vector:
            return 1
        elif current_Vector == new_Vector:
            return 0
        else:
            raise Exception("Unknown Error")