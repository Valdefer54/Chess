import pytest
from board import Board
from pieces.king import king
from pieces.rook import rook

@pytest.fixture
def board():
    b = Board()
    b.set_pieces_board()
    return b

def test_initial_board_no_check(board):
    assert not board.is_in_check("white")
    assert not board.is_in_check("black")

def test_check_by_rook(board):
    # Clear the board to set up a specific scenario
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]
    
    # Place a white king and a black rook in a check position
    white_king_piece = king("white", (3, 4))
    black_rook_piece = rook("black", (3, 7))
    
    board.startingBoard[3][4] = white_king_piece
    board.startingBoard[3][7] = black_rook_piece
    
    board.pieces = [white_king_piece, black_rook_piece]
    
    assert board.is_in_check("white")

def test_no_check_after_valid_move(board):
    # Perform a valid opening move for white
    board.move_piece((6, 4), (4, 4), "white") # White Pawn e2 to e4
    assert not board.is_in_check("white")
    
    # Perform a valid opening move for black
    board.move_piece((1, 4), (3, 4), "black") # Black Pawn e7 to e5
    assert not board.is_in_check("black")
    assert not board.is_in_check("white")

def test_king_cannot_move_into_check(board):
    # Clear the board
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]

    # Set up a scenario where the king is about to move into check
    white_king_piece = king("white", (0, 6))
    black_rook_piece = rook("black", (1, 7))
    board.startingBoard[0][6] = white_king_piece
    board.startingBoard[1][7] = black_rook_piece
    board.pieces = [white_king_piece, black_rook_piece]

    # Try to move the king into the rook's line of fire
    assert not board.move_piece((0, 6), (0, 7), "white")
    
    # Ensure the king has not moved
    assert board.startingBoard[0][6] == white_king_piece
    assert board.startingBoard[0][7] is None
