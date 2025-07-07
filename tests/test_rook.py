import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.set_pieces_board()

    def test_get_rook_has_moved_initial(self):
        self.assertFalse(self.board.get_rook_has_moved("white", "kingside"))
        self.assertFalse(self.board.get_rook_has_moved("white", "queenside"))
        self.assertFalse(self.board.get_rook_has_moved("black", "kingside"))
        self.assertFalse(self.board.get_rook_has_moved("black", "queenside"))

    def test_get_rook_has_moved_after_move(self):
        # Clear path for white kingside rook
        for i in range(1, 7):
            self.board.startingBoard[0][i] = None
        # Move white kingside rook
        self.board.move_piece((0, 7), (0, 5), "white")
        self.assertTrue(self.board.get_rook_has_moved("white", "kingside"))

        # Clear path for white queenside rook
        for i in range(1, 7):
            self.board.startingBoard[0][i] = None
        # Move white queenside rook
        self.board.move_piece((0, 0), (0, 2), "white")
        self.assertTrue(self.board.get_rook_has_moved("white", "queenside"))

        # Clear path for black kingside rook
        for i in range(1, 7):
            self.board.startingBoard[7][i] = None
        # Move black kingside rook
        self.board.move_piece((7, 7), (7, 5), "black")
        self.assertTrue(self.board.get_rook_has_moved("black", "kingside"))

        # Clear path for black queenside rook
        for i in range(1, 7):
            self.board.startingBoard[7][i] = None
        # Move black queenside rook
        self.board.move_piece((7, 0), (7, 2), "black")
        self.assertTrue(self.board.get_rook_has_moved("black", "queenside"))
