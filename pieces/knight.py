class Knight:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "Knight"
        self.symbol = "♞" if color == "white" else "♘"

    def get_theoretical_moves(self):
        moves = []
        row, col = self.position
        possible_moves = [
            (row - 2, col - 1), (row - 2, col + 1),
            (row - 1, col - 2), (row - 1, col + 2),
            (row + 1, col - 2), (row + 1, col + 2),
            (row + 2, col - 1), (row + 2, col + 1)
        ]
        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                moves.append(("move", move))
        return moves

    def move(self, new_position):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])

        # Knight moves in an L-shape: 2 squares in one direction and 1 square in the other
        if (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2):
            self.position = new_position
            return True

        return False