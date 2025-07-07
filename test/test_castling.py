import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from board import Board

def test_kingside_castling_white():
    board = Board()
    board.set_pieces_board()

    # Clear path for castling
    board.startingBoard[0][5] = None
    board.startingBoard[0][6] = None

    # Castle
    assert board.move_piece((0, 4), (0, 6), "white") is True

    # Assert king and rook positions
    assert board.startingBoard[0][6].name == "King"
    assert board.startingBoard[0][5].name == "Rook"
    assert board.startingBoard[0][4] is None
    assert board.startingBoard[0][7] is None

    # Assert has_moved flags
    assert board.startingBoard[0][6].has_moved is True
    assert board.startingBoard[0][5].has_moved is True

def test_queenside_castling_white():
    board = Board()
    board.set_pieces_board()

    # Clear path for castling
    board.startingBoard[0][1] = None
    board.startingBoard[0][2] = None
    board.startingBoard[0][3] = None

    # Castle
    assert board.move_piece((0, 4), (0, 2), "white") is True

    # Assert king and rook positions
    assert board.startingBoard[0][2].name == "King"
    assert board.startingBoard[0][3].name == "Rook"
    assert board.startingBoard[0][4] is None
    assert board.startingBoard[0][0] is None

    # Assert has_moved flags
    assert board.startingBoard[0][2].has_moved is True
    assert board.startingBoard[0][3].has_moved is True

def test_kingside_castling_black():
    board = Board()
    board.set_pieces_board()

    # Clear path for castling
    board.startingBoard[7][5] = None
    board.startingBoard[7][6] = None

    # Castle
    assert board.move_piece((7, 4), (7, 6), "black") is True

    # Assert king and rook positions
    assert board.startingBoard[7][6].name == "King"
    assert board.startingBoard[7][5].name == "Rook"
    assert board.startingBoard[7][4] is None
    assert board.startingBoard[7][7] is None

    # Assert has_moved flags
    assert board.startingBoard[7][6].has_moved is True
    assert board.startingBoard[7][5].has_moved is True

def test_queenside_castling_black():
    board = Board()
    board.set_pieces_board()

    # Clear path for castling
    board.startingBoard[7][1] = None
    board.startingBoard[7][2] = None
    board.startingBoard[7][3] = None

    # Castle
    assert board.move_piece((7, 4), (7, 2), "black") is True

    # Assert king and rook positions
    assert board.startingBoard[7][2].name == "King"
    assert board.startingBoard[7][3].name == "Rook"
    assert board.startingBoard[7][4] is None
    assert board.startingBoard[7][0] is None

    # Assert has_moved flags
    assert board.startingBoard[7][2].has_moved is True
    assert board.startingBoard[7][3].has_moved is True

def test_castling_blocked():
    board = Board()
    board.set_pieces_board()

    # Path is not clear
    board.startingBoard[0][6] = None

    # Attempt to castle
    assert board.move_piece((0, 4), (0, 6), "white") is False

def test_castling_king_moved():
    board = Board()
    board.set_pieces_board()

    # Clear path
    board.startingBoard[0][5] = None
    board.startingBoard[0][6] = None

    # Move king
    board.move_piece((0, 4), (0, 5), "white")
    board.move_piece((0, 5), (0, 4), "white")

    # Attempt to castle
    assert board.move_piece((0, 4), (0, 6), "white") is False

def test_castling_rook_moved():
    board = Board()
    board.set_pieces_board()

    # Clear path
    board.startingBoard[0][5] = None
    board.startingBoard[0][6] = None

    # Move rook
    board.move_piece((0, 7), (0, 6), "white")
    board.move_piece((0, 6), (0, 7), "white")

    # Attempt to castle
    assert board.move_piece((0, 4), (0, 6), "white") is False