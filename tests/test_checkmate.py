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
    # Classic back-rank mate position for white king
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]
    white_king = king("white", (7, 6)) # King on g1
    black_rook = rook("black", (7, 0)) # Rook on a1
    wp1 = Pawn("white", (6, 5))       # Pawn on f2
    wp2 = Pawn("white", (6, 6))       # Pawn on g2
    wp3 = Pawn("white", (6, 7))       # Pawn on h2

    board.startingBoard[7][6] = white_king
    board.startingBoard[7][0] = black_rook
    board.startingBoard[6][5] = wp1
    board.startingBoard[6][6] = wp2
    board.startingBoard[6][7] = wp3
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

def test_is_checkmate_back_rank_fen(board):
    # Corresponds to FEN: R5k1/5ppp/8/8/8/8/5PPP/6K1 b - - 1 1
    board.startingBoard = [[None for _ in range(8)] for _ in range(8)]
    
    # Piece setup
    white_rook = rook("white", (0, 0))
    black_king = king("black", (0, 6))
    
    bp1 = Pawn("black", (1, 5))
    bp2 = Pawn("black", (1, 6))
    bp3 = Pawn("black", (1, 7))
    
    wp1 = Pawn("white", (6, 5))
    wp2 = Pawn("white", (6, 6))
    wp3 = Pawn("white", (6, 7))
    white_king = king("white", (7, 6))

    # Place pieces on board
    board.startingBoard[0][0] = white_rook
    board.startingBoard[0][6] = black_king
    board.startingBoard[1][5] = bp1
    board.startingBoard[1][6] = bp2
    board.startingBoard[1][7] = bp3
    board.startingBoard[6][5] = wp1
    board.startingBoard[6][6] = wp2
    board.startingBoard[6][7] = wp3
    board.startingBoard[7][6] = white_king
    
    # Update piece list
    board.pieces = [
        white_rook, black_king, 
        bp1, bp2, bp3, 
        wp1, wp2, wp3, 
        white_king
    ]

    assert board.is_in_check("black")
    assert board.is_checkmate("black")
