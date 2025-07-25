from pieces.rook import rook
from pieces.knight import Knight
from pieces.bishop import bishop
from pieces.queen import queen
from pieces.king import king
from pieces.pawn import Pawn

class Board:
    def __init__(self):
                
        #white pieces instantiation
        self.white_rook_1 = rook("white", (0, 0))
        self.white_rook_2 = rook("white", (0, 7))
        self.white_knight_1 = Knight("white", (0, 1))
        self.white_knight_2 = Knight("white", (0, 6))
        self.white_bishop_1 = bishop("white", (0, 2))
        self.white_bishop_2 = bishop("white", (0, 5))
        self.white_queen = queen("white", (0, 3))
        self.white_king = king("white", (0, 4))
        self.white_pawn_1 = Pawn("white", (6, 0))
        self.white_pawn_2 = Pawn("white", (6, 1))
        self.white_pawn_3 = Pawn("white", (6, 2))
        self.white_pawn_4 = Pawn("white", (6, 3))
        self.white_pawn_5 = Pawn("white", (6, 4))
        self.white_pawn_6 = Pawn("white", (6, 5))
        self.white_pawn_7 = Pawn("white", (6, 6))
        self.white_pawn_8 = Pawn("white", (6, 7))

        #black pieces instantiation
        self.black_rook_1 = rook("black", (7, 0))
        self.black_rook_2 = rook("black", (7, 7))
        self.black_knight_1 = Knight("black", (7, 1))
        self.black_knight_2 = Knight("black", (7, 6))
        self.black_bishop_1 = bishop("black", (7, 2))
        self.black_bishop_2 = bishop("black", (7, 5))
        self.black_queen = queen("black", (7, 3))
        self.black_king = king("black", (7, 4))
        self.black_pawn_1 = Pawn("black", (1, 0))
        self.black_pawn_2 = Pawn("black", (1, 1))
        self.black_pawn_3 = Pawn("black", (1, 2))
        self.black_pawn_4 = Pawn("black", (1, 3))
        self.black_pawn_5 = Pawn("black", (1, 4))
        self.black_pawn_6 = Pawn("black", (1, 5))
        self.black_pawn_7 = Pawn("black", (1, 6))
        self.black_pawn_8 = Pawn("black", (1, 7))

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
        for piece in self.pieces:
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

    def get_valid_moves(self, piece_pos):
        piece = self.startingBoard[piece_pos[0]][piece_pos[1]]
        if not piece:
            return []

        theoretical_moves = piece.get_theoretical_moves()
        valid_moves = []

        for move_type, dest_pos in theoretical_moves:
            dest_row, dest_col = dest_pos
            target_piece = self.startingBoard[dest_row][dest_col]

            if piece.name == "Pawn":
                if move_type == "forward":
                    if not target_piece:
                        valid_moves.append(dest_pos)
                elif move_type == "double_forward":
                    path_row = piece_pos[0] + piece.direction
                    if not target_piece and not self.startingBoard[path_row][dest_col]:
                        valid_moves.append(dest_pos)
                elif move_type == "capture":
                    if target_piece and target_piece.color != piece.color:
                        valid_moves.append(dest_pos)
            elif piece.name == "Knight":
                if not target_piece or target_piece.color != piece.color:
                    valid_moves.append(dest_pos)
            elif piece.name == "King":
                if not target_piece or target_piece.color != piece.color:
                    valid_moves.append(dest_pos)
            elif piece.name in ["Rook", "Bishop", "Queen"]:
                if self.is_path_clear(piece_pos, dest_pos):
                    if not target_piece or target_piece.color != piece.color:
                        valid_moves.append(dest_pos)

        return valid_moves

    def move_piece(self, from_pos, to_pos, current_player_color):
        piece_to_move = self.startingBoard[from_pos[0]][from_pos[1]]

        if not piece_to_move:
            return False # No piece at from_pos

        if piece_to_move.color != current_player_color:
            return False # Piece does not belong to current player

        # Handle castling
        if piece_to_move.name == "King" and abs(from_pos[1] - to_pos[1]) == 2:
            side = "kingside" if to_pos[1] > from_pos[1] else "queenside"
            return self.castle(piece_to_move.color, side)

        valid_moves = self.get_valid_moves(from_pos)
        if to_pos not in valid_moves:
            return False

        # Store original state to revert if move is illegal
        target_piece = self.startingBoard[to_pos[0]][to_pos[1]]
        original_pos = piece_to_move.position

        # Make the move
        self.startingBoard[to_pos[0]][to_pos[1]] = piece_to_move
        self.startingBoard[from_pos[0]][from_pos[1]] = None
        piece_to_move.position = to_pos

        # If the move results in check, it's illegal. Revert and return False.
        if self.is_in_check(current_player_color):
            self.startingBoard[from_pos[0]][from_pos[1]] = piece_to_move
            self.startingBoard[to_pos[0]][to_pos[1]] = target_piece
            piece_to_move.position = original_pos
            return False

        # Handle capture
        if target_piece:
            pass # Removed print statement
        if piece_to_move.name == "Pawn":
            piece_to_move.has_moved = True
        elif piece_to_move.name == "King":
            piece_to_move.has_moved = True
        elif piece_to_move.name == "Rook":
            piece_to_move.has_moved = True

        return True

    def get_king_has_moved(self, color):
        for piece in self.pieces:
            if piece.name == "King" and piece.color == color:
                return piece.has_moved
        return False # Should not happen if kings are always on the board

    def get_rook_has_moved(self, color, side):
        for piece in self.pieces:
            if piece.name == "Rook" and piece.color == color:
                if (side == "kingside" and (piece.initial_position == (0, 7) or piece.initial_position == (7, 7))) or \
                   (side == "queenside" and (piece.initial_position == (0, 0) or piece.initial_position == (7, 0))):
                    return piece.has_moved
        return False # Should not happen if rooks are always on the board

    def is_path_clear(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # Determine the direction of movement
        row_step = 0
        if end_row > start_row:
            row_step = 1
        elif end_row < start_row:
            row_step = -1
            
        col_step = 0
        if end_col > start_col:
            col_step = 1
        elif end_col < start_col:
            col_step = -1
            
        current_row, current_col = start_row + row_step, start_col + col_step
        
        # Iterate over the path
        while (current_row, current_col) != (end_row, end_col):
            if self.startingBoard[current_row][current_col] is not None:
                return False  # Path is blocked
            current_row += row_step
            current_col += col_step
            
        return True

    def castle(self, color, side):
        king_moved = self.get_king_has_moved(color)
        rook_moved = self.get_rook_has_moved(color, side)

        if king_moved or rook_moved:
            return False

        king_pos = None
        rook_pos = None
        for piece in self.pieces:
            if piece.name == "King" and piece.color == color:
                king_pos = piece.position
            if piece.name == "Rook" and piece.color == color:
                if (side == "kingside" and (piece.initial_position == (0, 7) or piece.initial_position == (7, 7))) or \
                   (side == "queenside" and (piece.initial_position == (0, 0) or piece.initial_position == (7, 0))):
                    rook_pos = piece.position

        if not self.is_path_clear(king_pos, rook_pos):
            return False

        # Move pieces
        if side == "kingside":
            new_king_col = king_pos[1] + 2
            new_rook_col = new_king_col - 1
        else: # queenside
            new_king_col = king_pos[1] - 2
            new_rook_col = new_king_col + 1

        king_row = king_pos[0]
        
        # Update board
        king = self.startingBoard[king_pos[0]][king_pos[1]]
        rook = self.startingBoard[rook_pos[0]][rook_pos[1]]
        
        self.startingBoard[king_row][new_king_col] = king
        self.startingBoard[king_row][new_rook_col] = rook
        self.startingBoard[king_pos[0]][king_pos[1]] = None
        self.startingBoard[rook_pos[0]][rook_pos[1]] = None

        # Update piece positions and has_moved
        king.position = (king_row, new_king_col)
        rook.position = (king_row, new_rook_col)
        king.has_moved = True
        rook.has_moved = True

        return True

    def is_in_check(self, color):
        king_pos = None
        for r in range(8):
            for c in range(8):
                piece = self.startingBoard[r][c]
                if piece and piece.name == "King" and piece.color == color:
                    king_pos = (r, c)
                    break
            if king_pos:
                break

        if not king_pos:
            return False

        for r in range(8):
            for c in range(8):
                piece = self.startingBoard[r][c]
                if piece and piece.color != color:
                    valid_moves = self.get_valid_moves((r, c))
                    if king_pos in valid_moves:
                        return True
        return False

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False

        for r in range(8):
            for c in range(8):
                piece = self.startingBoard[r][c]
                if piece and piece.color == color:
                    valid_moves = self.get_valid_moves((r, c))
                    for move in valid_moves:
                        from_pos = (r, c)
                        to_pos = move
                        target_piece = self.startingBoard[to_pos[0]][to_pos[1]]
                        
                        original_pos = piece.position
                        
                        # Temporarily make the move on the board
                        self.startingBoard[to_pos[0]][to_pos[1]] = piece
                        self.startingBoard[from_pos[0]][from_pos[1]] = None
                        piece.position = to_pos

                        is_still_in_check = self.is_in_check(color)

                        # Revert the board to its original state
                        self.startingBoard[from_pos[0]][from_pos[1]] = piece
                        self.startingBoard[to_pos[0]][to_pos[1]] = target_piece
                        piece.position = original_pos

                        if not is_still_in_check:
                            return False  # Found a legal move that gets out of check

        return True