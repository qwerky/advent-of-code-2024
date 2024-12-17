from Grid import Grid

class Block:

    def __init__(self, row, col):
        self.row = row
        self.col = col


    def __repr__(self):
        return f"Block at r{self.row} c{self.col}"


    def getPushed(self, direction):
        if direction == "<":
            return [(self.row, self.col-1)]
        elif direction == ">":
            return [(self.row, self.col+2)]
        elif direction == "^":
            return [(self.row-1, self.col), (self.row-1, self.col+1)]
        elif direction == "v":
            return [(self.row+1, self.col), (self.row+1, self.col+1)]
