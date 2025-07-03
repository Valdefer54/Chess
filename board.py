from pieces import pawn, rook, knight, bishop, queen
from pieces.rook import rook
from pieces.knight import knight
from pieces.bishop import bishop
from pieces.queen import queen
from pieces.king import king
from pieces.pawn import Pawn

# Initialize the chess pieces with their respective colors and positions at the start of the game
white_rook_1 = rook("white", (0, 0))
white_rook_2 = rook("white", (0, 7))
white_knight_1 = knight("white", (0, 1))
white_knight_2 = knight("white", (0, 6))
white_bishop_1 = bishop("white", (0, 2))
white_bishop_2 = bishop("white", (0, 5))
white_queen = queen("white", (0, 3))
white_king = king("white", (0, 4))
white_pawn_1 = Pawn("white", (1, 0))
white_pawn_2 = Pawn("white", (1, 1))
white_pawn_3 = Pawn("white", (1, 2))
white_pawn_4 = Pawn("white", (1, 3))
white_pawn_5 = Pawn("white", (1, 4))
white_pawn_6 = Pawn("white", (1, 5))
white_pawn_7 = Pawn("white", (1, 6))
white_pawn_8 = Pawn("white", (1, 7))

black_rook_1 = rook("black", (7, 0))
black_rook_2 = rook("black", (7, 7))
black_knight_1 = knight("black", (7, 1))
black_knight_2 = knight("black", (7, 6))
black_bishop_1 = bishop("black", (7, 2))
black_bishop_2 = bishop("black", (7, 5))
black_queen = queen("black", (7, 3))
black_king = king("black", (7, 4))
black_pawn_1 = Pawn("black", (6, 0))
black_pawn_2 = Pawn("black", (6, 1))
black_pawn_3 = Pawn("black", (6, 2))
black_pawn_4 = Pawn("black", (6, 3))
black_pawn_5 = Pawn("black", (6, 4))
black_pawn_6 = Pawn("black", (6, 5))
black_pawn_7 = Pawn("black", (6, 6))
black_pawn_8 = Pawn("black", (6, 7))

# List of all pieces
pieces = [
            white_rook_1, white_rook_2, white_knight_1, white_knight_2, white_bishop_1, white_bishop_2,
            white_queen, white_king, white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4,
            white_pawn_5, white_pawn_6, white_pawn_7, white_pawn_8,
            black_rook_1, black_rook_2, black_knight_1, black_knight_2, black_bishop_1, black_bishop_2,
            black_queen, black_king, black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
            black_pawn_5, black_pawn_6, black_pawn_7, black_pawn_8
        ]

class Board:
    def __init__(self,pieces):
                
        #white pieces instantiation
        self.white_rook_1 = rook("white", (0, 0))
        self.white_rook_2 = rook("white", (0, 7))
        self.white_knight_1 = knight("white", (0, 1))
        self.white_knight_2 = knight("white", (0, 6))
        self.white_bishop_1 = bishop("white", (0, 2))
        self.white_bishop_2 = bishop("white", (0, 5))
        self.white_queen = queen("white", (0, 3))
        self.white_king = king("white", (0, 4))
        self.white_pawn_1 = Pawn("white", (1, 0))
        self.white_pawn_2 = Pawn("white", (1, 1))
        self.white_pawn_3 = Pawn("white", (1, 2))
        self.white_pawn_4 = Pawn("white", (1, 3))
        self.white_pawn_5 = Pawn("white", (1, 4))
        self.white_pawn_6 = Pawn("white", (1, 5))
        self.white_pawn_7 = Pawn("white", (1, 6))
        self.white_pawn_8 = Pawn("white", (1, 7))

        #black pieces instantiation
        self.black_rook_1 = rook("black", (7, 0))
        self.black_rook_2 = rook("black", (7, 7))
        self.black_knight_1 = knight("black", (7, 1))
        self.black_knight_2 = knight("black", (7, 6))
        self.black_bishop_1 = bishop("black", (7, 2))
        self.black_bishop_2 = bishop("black", (7, 5))
        self.black_queen = queen("black", (7, 3))
        self.black_king = king("black", (7, 4))
        self.black_pawn_1 = Pawn("black", (6, 0))
        self.black_pawn_2 = Pawn("black", (6, 1))
        self.black_pawn_3 = Pawn("black", (6, 2))
        self.black_pawn_4 = Pawn("black", (6, 3))
        self.black_pawn_5 = Pawn("black", (6, 4))
        self.black_pawn_6 = Pawn("black", (6, 5))
        self.black_pawn_7 = Pawn("black", (6, 6))
        self.black_pawn_8 = Pawn("black", (6, 7))

        # Initialize the chess pieces with their respective colors and positions at the start of the game
        self.pieces = [
            self.white_rook_1, self.white_rook_2, self.white_knight_1, self.white_knight_2, self.white_bishop_1, self.white_bishop_2,
            self.white_queen, self.white_king, self.white_pawn_1, self.white_pawn_2, self.white_pawn_3, self.white_pawn_4,
            self.white_pawn_5, self.white_pawn_6, self.white_pawn_7, self.white_pawn_8,
            self.black_rook_1, self.black_rook_2, self.black_knight_1, self.black_knight_2, self.black_bishop_1, self.black_bishop_2,
            self.black_queen, self.black_king, self.black_pawn_1, self.black_pawn_2, self.black_pawn_3, self.black_pawn_4,
            self.black_pawn_5, self.black_pawn_6, self.black_pawn_7, self.black_pawn_8
        ]
        self.startingBoard = [[None for _ in range(8)] for _ in range(8)]

    # Set the pieces on the board
    def set_pieces_board(self):
        for piece in pieces:
            row, col = piece.position  # Usa el atributo position solo para inicializar
            self.startingBoard[row][col] = piece

    def boardPrinter(self):
        # Imprime las letras de las columnas
        print("   " + "  ".join("a b c d e f g h".split()))
        for i, row in enumerate(self.startingBoard):
            fila = 8 - i
            row_str = []
            for piece in row:
                symbol = piece.symbol if piece else " "
                row_str.append(symbol)
            print(f"{fila}  " + "  ".join(row_str) + f"  {fila}")
        print("   " + "  ".join("a b c d e f g h".split()))

    def is_same_side(self, from_pos, to_pos):
        from_piece = self.startingBoard[from_pos[0]][from_pos[1]]
        to_piece = self.startingBoard[to_pos[0]][to_pos[1]]
        if to_piece is None:
            return False
        return from_piece.color == to_piece.color

    def move_piece(self, from_pos, to_pos, piece):
        if self.is_same_side(from_pos, to_pos):
            print("Cannot move to a square occupied by a piece of the same color.")
            return False
        if piece.color == "white":
            row, col = to_pos
            if self.startingBoard[row][col] is not None:
                if self.startingBoard[row][col].color == "black":
                    self.startingBoard[row][col] = None
                else:
                    print("Cannot capture your own piece.")
                    return False
        else:
            row, col = to_pos
            if self.startingBoard[row][col] is not None:
                if self.startingBoard[row][col].color == "white":
                    self.startingBoard[row][col] = None
                else:
                    print("Cannot capture your own piece.")
                    return False
        # Move the piece
        self.startingBoard[to_pos[0]][to_pos[1]] = piece
        self.startingBoard[from_pos[0]][from_pos[1]] = None
        piece.position = to_pos
    
tablero = Board(pieces)
tablero.set_pieces_board()
tablero.boardPrinter()