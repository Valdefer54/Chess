class king:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "King"
        self.symbol = "♚" if color == "white" else "♔"
        self.has_moved = False

    def gmove(self, new_position):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])

        # King moves one square in any direction
        if (x_diff <= 1 and y_diff <= 1):
            self.position = new_position
            return True

        return False

    def get_theoretical_moves(self):
        moves = []
        for r_offset in [-1, 0, 1]:
            for c_offset in [-1, 0, 1]:
                if r_offset == 0 and c_offset == 0:
                    continue
                new_row, new_col = self.position[0] + r_offset, self.position[1] + c_offset
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append(("move", (new_row, new_col)))
        return moves