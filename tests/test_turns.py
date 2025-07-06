import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_chess_game

class TestTurnLogic(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('board.Board.boardPrinter')
    def test_turn_changes_on_valid_move(self, mock_board_printer, mock_stdout):
        # Simulate input for a valid move by white, then a valid move by black
        # and then an exit command.
        # White moves e2 e4
        # Black moves e7 e5
        # Exit
        mock_input = ['e2 e4', 'e7 e5', 'exit']
        with patch('builtins.input', side_effect=mock_input) as mock_input_func:
            run_chess_game(input_function=mock_input_func, print_function=mock_stdout.write)

        output = mock_stdout.getvalue()

        # Check if turn changes correctly
        self.assertIn("Turno del jugador: white", output)
        self.assertIn("Turno del jugador: black", output)
        self.assertIn("Saliendo del juego.", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('board.Board.boardPrinter')
    def test_turn_does_not_change_on_invalid_move_wrong_piece(self, mock_board_printer, mock_stdout):
        # Simulate input for white trying to move a black piece, then exit
        # White tries to move e7 e5 (black's pawn)
        # Exit
        mock_input = ['e7 e5', 'exit']
        with patch('builtins.input', side_effect=mock_input) as mock_input_func:
            run_chess_game(input_function=mock_input_func, print_function=mock_stdout.write)

        output = mock_stdout.getvalue()

        # Check if turn remains white after invalid move
        self.assertIn("Turno del jugador: white", output)
        self.assertIn("--- Movimiento inválido. Inténtalo de nuevo. ---", output)
        # Ensure 'Turno del jugador: black' does not appear before exit
        self.assertNotIn("Turno del jugador: black", output.split('Saliendo del juego.')[0])

    @patch('sys.stdout', new_callable=StringIO)
    @patch('board.Board.boardPrinter')
    def test_turn_does_not_change_on_invalid_move_no_piece(self, mock_board_printer, mock_stdout):
        # Simulate input for white trying to move from an empty square, then exit
        # White tries to move a4 a5 (empty square)
        # Exit
        mock_input = ['a4 a5', 'exit']
        with patch('builtins.input', side_effect=mock_input) as mock_input_func:
            run_chess_game(input_function=mock_input_func, print_function=mock_stdout.write)

        output = mock_stdout.getvalue()

        # Check if turn remains white after invalid move
        self.assertIn("Turno del jugador: white", output)
        self.assertIn("--- Movimiento inválido. Inténtalo de nuevo. ---", output)
        # Ensure 'Turno del jugador: black' does not appear before exit
        self.assertNotIn("Turno del jugador: black", output.split('Saliendo del juego.')[0])

    @patch('sys.stdout', new_callable=StringIO)
    @patch('board.Board.boardPrinter')
    def test_turn_does_not_change_on_invalid_move_format(self, mock_board_printer, mock_stdout):
        # Simulate input for white entering invalid format, then exit
        # White enters 'invalid move'
        # Exit
        mock_input = ['invalid move', 'exit']
        with patch('builtins.input', side_effect=mock_input) as mock_input_func:
            run_chess_game(input_function=mock_input_func, print_function=mock_stdout.write)

        output = mock_stdout.getvalue()

        # Check if turn remains white after invalid move
        self.assertIn("Turno del jugador: white", output)
        self.assertIn("--- Movimiento inválido. Inténtalo de nuevo. ---", output)
        # Ensure 'Turno del jugador: black' does not appear before exit
        self.assertNotIn("Turno del jugador: black", output.split('Saliendo del juego.')[0])


if __name__ == '__main__':
    unittest.main()