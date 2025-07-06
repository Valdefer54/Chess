class Pawn:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "Pawn"
        self.symbol = "♟" if color == "white" else "♙"
        self.has_moved = False # Used to determine if a double move is allowed
        # White moves from low row index to high, Black from high to low
        self.direction = 1 if self.color == "white" else -1

    def get_theoretical_moves(self):
        """
        Returns a list of all theoretically possible move destinations for the pawn,
        without considering the state of the board (e.g., blocking pieces).
        This includes single and double forward moves, and diagonal captures.
        """
        moves = []
        current_row, current_col = self.position

        # 1. Forward moves
        # Single square forward
        forward_one_row = current_row + self.direction
        if 0 <= forward_one_row <= 7:
            moves.append(("forward", (forward_one_row, current_col)))

        # Double square forward (only if it has not moved yet)
        if not self.has_moved:
            forward_two_row = current_row + 2 * self.direction
            if 0 <= forward_two_row <= 7:
                moves.append(("double_forward", (forward_two_row, current_col)))

        # 2. Capture moves (diagonal)
        capture_row = current_row + self.direction
        if 0 <= capture_row <= 7:
            # Capture left
            capture_col_left = current_col - 1
            if 0 <= capture_col_left <= 7:
                moves.append(("capture", (capture_row, capture_col_left)))
            # Capture right
            capture_col_right = current_col + 1
            if 0 <= capture_col_right <= 7:
                moves.append(("capture", (capture_row, capture_col_right)))
        
        return moves