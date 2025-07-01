class knight:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "knight"
        self.symbol = "♞" if color == "white" else "♘"

    def move(self, new_position):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])

        # Knight moves in an L-shape: 2 squares in one direction and 1 square in the other
        if (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2):
            self.position = new_position
            return True

        return False