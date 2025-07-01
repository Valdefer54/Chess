class Pawn:
    def __init__(self, color, position, allow_double_move=True, alive=True):
        self.color = color
        self.position = position
        self.name = "pawn"
        self.symbol = "♟" if color == "white" else "♙"
        self.allow_double_move = allow_double_move
        self.alive = alive
        self.direction = 1 if color == "white" else -1
    
    def move(self, new_position):
       
        if self.allow_double_move and self.position[1] == (1 if self.color == "white" else 6):
            if new_position[0] == self.position[0] and new_position[1] == self.position[1] + 2 * self.direction:
                self.position = new_position
                return True
        elif new_position[0] == self.position[0] and new_position[1] == self.position[1] + self.direction:
            self.position = new_position
            return True

        return False

