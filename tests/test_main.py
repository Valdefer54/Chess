import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from board import Board

class TestMain(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.set_pieces_board()

    def test_game_simulation(self):
        # White's moves
        self.assertTrue(self.board.move_piece((6, 4), (4, 4), "white"))  # e4
        self.assertTrue(self.board.move_piece((0, 6), (2, 5), "white"))  # Nf3
        self.assertTrue(self.board.move_piece((6, 3), (4, 3), "white"))  # d4

        # Black's moves
        self.assertTrue(self.board.move_piece((1, 4), (3, 4), "black"))  # e5
        self.assertTrue(self.board.move_piece((7, 1), (5, 2), "black"))  # Nc6
        self.assertTrue(self.board.move_piece((1, 3), (3, 3), "black"))  # d5

        # Assert final positions
        self.assertEqual(self.board.startingBoard[3][4].name, "Pawn")
        self.assertEqual(self.board.startingBoard[2][5].name, "Knight")
        self.assertEqual(self.board.startingBoard[3][3].name, "Pawn")
        self.assertEqual(self.board.startingBoard[4][4].name, "Pawn")
        self.assertEqual(self.board.startingBoard[5][2].name, "Knight")
        self.assertEqual(self.board.startingBoard[4][3].name, "Pawn")

    if __name__ == '__main__':
        unittest.main()
