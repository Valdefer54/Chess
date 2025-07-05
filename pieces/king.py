class king:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "king"
        self.symbol = "♚" if color == "white" else "♔"

    def gmove(self, new_position):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])

        # King moves one square in any direction
        if (x_diff <= 1 and y_diff <= 1):
            self.position = new_position
            return True

        return False