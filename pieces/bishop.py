class bishop:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = "Bishop"
        self.symbol = "♝" if color == "white" else "♗"
    
    def move(self, new_position):
        x_diff = abs(new_position[0] - self.position[0])
        y_diff = abs(new_position[1] - self.position[1])

        # Bishop moves diagonally: equal change in both x and y coordinates
        if x_diff == y_diff:
            self.position = new_position
            return True

        return False
