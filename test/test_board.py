import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board([])  # El constructor ya crea las piezas internamente
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

    def test_is_same_side_true(self):
        # Dos piezas blancas
        from_pos = (1, 0)  # Peón blanco
        to_pos = (1, 1)    # Peón blanco
        self.assertTrue(self.board.is_same_side(from_pos, to_pos))

    def test_is_same_side_false(self):
        # Pieza blanca y negra
        from_pos = (1, 0)  # Peón blanco
        to_pos = (6, 0)    # Peón negro
        self.assertFalse(self.board.is_same_side(from_pos, to_pos))

    def test_is_same_side_none(self):
        # Pieza y casilla vacía
        from_pos = (1, 0)
        to_pos = (3, 3)
        self.assertFalse(self.board.is_same_side(from_pos, to_pos))

    def test_move_piece_capture(self):
        # Mueve peón blanco a posición de peón negro (captura)
        from_pos = (1, 0)
        to_pos = (6, 0)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        self.board.move_piece(from_pos, to_pos, piece)
        self.assertIs(self.board.startingBoard[to_pos[0]][to_pos[1]], piece)
        self.assertIsNone(self.board.startingBoard[from_pos[0]][from_pos[1]])
        self.assertEqual(piece.position, to_pos)

    def test_move_piece_same_side(self):
        # Intenta mover peón blanco a casilla ocupada por otro blanco
        from_pos = (1, 0)
        to_pos = (1, 1)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        result = self.board.move_piece(from_pos, to_pos, piece)
        self.assertFalse(result)
        self.assertIs(self.board.startingBoard[from_pos[0]][from_pos[1]], piece)

    def test_move_piece_empty(self):
        # Mueve peón blanco a casilla vacía
        from_pos = (1, 0)
        to_pos = (3, 0)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        self.board.move_piece(from_pos, to_pos, piece)
        self.assertIs(self.board.startingBoard[to_pos[0]][to_pos[1]], piece)
        self.assertIsNone(self.board.startingBoard[from_pos[0]][from_pos[1]])
        self.assertEqual(piece.position, to_pos)

import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board([])  # El constructor ya crea las piezas internamente
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

    def test_is_same_side_true(self):
        # Dos piezas blancas
        from_pos = (1, 0)  # Peón blanco
        to_pos = (1, 1)    # Peón blanco
        self.assertTrue(self.board.is_same_side(from_pos, to_pos))

    def test_is_same_side_false(self):
        # Pieza blanca y negra
        from_pos = (1, 0)  # Peón blanco
        to_pos = (6, 0)    # Peón negro
        self.assertFalse(self.board.is_same_side(from_pos, to_pos))

    def test_is_same_side_none(self):
        # Pieza y casilla vacía
        from_pos = (1, 0)
        to_pos = (3, 3)
        self.assertFalse(self.board.is_same_side(from_pos, to_pos))

    def test_move_piece_capture(self):
        # Mueve peón blanco a posición de peón negro (captura)
        from_pos = (1, 0)
        to_pos = (6, 0)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        self.board.move_piece(from_pos, to_pos, piece)
        self.assertIs(self.board.startingBoard[to_pos[0]][to_pos[1]], piece)
        self.assertIsNone(self.board.startingBoard[from_pos[0]][from_pos[1]])
        self.assertEqual(piece.position, to_pos)

    def test_move_piece_same_side(self):
        # Intenta mover peón blanco a casilla ocupada por otro blanco
        from_pos = (1, 0)
        to_pos = (1, 1)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        result = self.board.move_piece(from_pos, to_pos, piece)
        self.assertFalse(result)
        self.assertIs(self.board.startingBoard[from_pos[0]][from_pos[1]], piece)

    def test_move_piece_empty(self):
        # Mueve peón blanco a casilla vacía
        from_pos = (1, 0)
        to_pos = (3, 0)
        piece = self.board.startingBoard[from_pos[0]][from_pos[1]]
        self.board.move_piece(from_pos, to_pos, piece)
        self.assertIs(self.board.startingBoard[to_pos[0]][to_pos[1]], piece)
        self.assertIsNone(self.board.startingBoard[from_pos[0]][from_pos[1]])
        self.assertEqual(piece.position, to_pos)

if __name__ == '__main__':
    unittest.main()