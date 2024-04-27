import ChessPython
import unittest 
new_board = ChessPython.Board()

new_board.addChessPiece(ChessPython.BlackKing(), "a8")
new_board.addChessPiece(ChessPython.WhiteKing(), "c5")
new_board.addChessPiece(ChessPython.WhitePawn(), "d6")
new_board.addChessPiece(ChessPython.WhitePawn(), "c6")
new_board.addChessPiece(ChessPython.BlackPawn(), "b5")
new_board.addChessPiece(ChessPython.BlackPawn(), "b4")
new_game = ChessPython.Game(new_board)

class Test_MoveChessGeneral(unittest.TestCase):
    def test_InvalidMove_3Chars(self):
        test_variable ={
            ("K2a", False),
            ("Ka9", False),
            ("Kj5", False),
            ("cK8", False),
            ("0c6", False),
        }

        for move_code, expected_result in test_variable:
            with self.subTest(move_code=move_code, expected_result=expected_result):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, expected_result)
                
    def test_InvalidMove_2Chars(self):
        test_variable ={
            ("K1", False),
            ("1c", False),
            ("c9", False),
            ("dd", False),
            ("11", False),
            }
        
        for move_code, expected_result in test_variable:
            with self.subTest(move_code=move_code, expected_result=expected_result):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, expected_result)

    
    def test_InvalidMove_4Char(self):
        test_variable ={
            ("c#d2", False),
            ("a2xd", False),
            ("K=Q8", False),
            ("a8+b", False),
            ("Kx1Q", False),
        }

        for move_code, expected_result in test_variable:
            with self.subTest(move_code=move_code, expected_result=expected_result):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, expected_result)


    def test_InvalidMove_NotInRangeChars(self):
        test_variable ={
            ("b2x7x7xa3", False),
            ("", False),
            ("c", False),
            ("c7xd9=Q", False),
            ("1", False),
        }

        for move_code, expected_result in test_variable:
            with self.subTest(move_code=move_code, expected_result=expected_result):
                result = new_game.MoveChessPiece(move_code)
                self.assertEqual(result, expected_result)
