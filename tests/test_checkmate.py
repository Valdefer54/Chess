import pytest
from board import Board
from pieces.king import king
from pieces.queen import queen
from pieces.rook import rook
from pieces.pawn import Pawn
from pieces.bishop import bishop

@pytest.fixture
def board():
    b = Board()
    return b

def test_is_checkmate_back_rank(board):
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]
    white_king = king("white", (0, 6))
    black_rook = rook("black", (0, 4))
    wp1 = Pawn("white", (1, 5))
    wp2 = Pawn("white", (1, 6))
    wp3 = Pawn("white", (1, 7))

    board.startingBoard[0][6] = white_king
    board.startingBoard[0][4] = black_rook
    board.startingBoard[1][5] = wp1
    board.startingBoard[1][6] = wp2
    board.startingBoard[1][7] = wp3
    board.pieces = [white_king, black_rook, wp1, wp2, wp3]

    assert board.is_in_check("white")
    assert board.is_checkmate("white")

def test_is_not_checkmate_can_capture(board):
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]
    white_king = king("white", (0, 0))
    black_rook = rook("black", (0, 1))
    white_rook = rook("white", (7, 1))

    board.startingBoard[0][0] = white_king
    board.startingBoard[0][1] = black_rook
    board.startingBoard[7][1] = white_rook
    board.pieces = [white_king, black_rook, white_rook]

    assert board.is_in_check("white")
    assert not board.is_checkmate("white")

def test_is_not_checkmate_can_block(board):
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]
    white_king = king("white", (0, 0))
    black_rook = rook("black", (0, 7))
    white_bishop_piece = bishop("white", (1, 1))

    board.startingBoard[0][0] = white_king
    board.startingBoard[0][7] = black_rook
    board.startingBoard[1][1] = white_bishop_piece
    board.pieces = [white_king, black_rook, white_bishop_piece]

    assert board.is_in_check("white")
    assert not board.is_checkmate("white")