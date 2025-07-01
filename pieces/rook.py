class rook:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "rook"
        self.symbol = "♜" if color == "white" else "♖"

    def move(self, new_position):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])

        # Rook moves in straight lines: either x or y coordinate changes, not both
        if (x_diff == 0 and y_diff > 0) or (y_diff == 0 and x_diff > 0):
            self.position = new_position
            return True

        return False