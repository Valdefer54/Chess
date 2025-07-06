import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.set_pieces_board()

    def test_set_pieces_board(self):
        # Verifica que todas las piezas estén en su posición inicial
        for piece in self.board.pieces:
            row, col = piece.position
            self.assertIs(self.board.startingBoard[row][col], piece)

    def test_boardPrinter(self):
        # Solo verifica que no lance excepción al imprimir
        try:
            self.board.boardPrinter()
        except Exception as e:
            self.fail(f"boardPrinter lanzó una excepción: {e}")

    

    def test_move_piece_capture(self):
        # Setup: Place a white pawn and a black pawn for capture scenario
        # White pawn at (6,0)
        white_pawn = self.board.startingBoard[6][0]
        # Black pawn at (1,1)
        black_pawn_to_capture = self.board.startingBoard[1][1]

        # Temporarily move black pawn to a capturable position for white pawn
        self.board.startingBoard[5][1] = black_pawn_to_capture
        black_pawn_to_capture.position = (5,1)
        self.board.startingBoard[1][1] = None # Clear original position

        from_pos = (6, 0) # White pawn
        to_pos = (5, 1) # Black pawn to capture
        piece_to_move = self.board.startingBoard[from_pos[0]][from_pos[1]] # This is the white pawn

        self.board.move_piece(from_pos, to_pos, "white")

        self.assertEqual(self.board.startingBoard[to_pos[0]][to_pos[1]], piece_to_move)
        self.assertIsNone(self.board.startingBoard[from_pos[0]][from_pos[1]])
        self.assertEqual(piece_to_move.position, to_pos)

    def test_move_piece_same_side(self):
        # Intenta mover peón blanco a casilla ocupada por otro blanco
        from_pos = (1, 0)
        to_pos = (1, 1)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        result = self.board.move_piece(from_pos, to_pos, "white")
        self.assertFalse(result)
        self.assertEqual(self.board.startingBoard[from_pos[0]][from_pos[1]], piece)

    def test_move_piece_empty(self):
        # Mueve peón blanco a casilla vacía
        from_pos = (6, 0)
        to_pos = (4, 0)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        self.board.move_piece(from_pos, to_pos, "white")
        self.assertEqual(self.board.startingBoard[to_pos[0]][to_pos[1]], piece)
        self.assertIsNone(self.board.startingBoard[from_pos[0]][from_pos[1]])
        self.assertEqual(piece.position, to_pos)

