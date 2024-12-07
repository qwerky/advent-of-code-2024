class Grid:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].strip())
        
        self.grid = []
        for line in lines:
            self.grid.append(list(line.strip()))

        self.path = []
        self.locations = set()

        for index in range(len(self.grid)):
            if "^" in self.grid[index]:
                self.guardRow = index
                self.guardCol = self.grid[index].index("^")

        self.direction = "^"
        self.path.append((self.guardRow, self.guardCol, self.direction))
        self.locations.add((self.guardRow, self.guardCol))


    def print(self):
        for line in self.grid:
            print(line)


    def turn(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"


    def stepWithoutRecording(self):
        """
        Takes a step, returns false if the step takes us off the grid
        """
        if self.direction == "^":
            if self.guardRow == 0:
                return False
            elif self.grid[self.guardRow-1][self.guardCol] == "#" or self.grid[self.guardRow-1][self.guardCol] == "O":
                self.turn()
            else:
                self.guardRow += -1
        elif self.direction == "v":
            if self.guardRow == self.height-1:
                return False
            elif self.grid[self.guardRow+1][self.guardCol] == "#" or self.grid[self.guardRow+1][self.guardCol] == "O":
                self.turn()
            else:
                self.guardRow += 1
        elif self.direction == "<":
            if self.guardCol == 0:
                return False
            elif self.grid[self.guardRow][self.guardCol-1] == "#" or self.grid[self.guardRow][self.guardCol-1] == "O":
                self.turn()
            else:
                self.guardCol += -1
        elif self.direction == ">":
            if self.guardCol == self.width-1:
                return False
            elif self.grid[self.guardRow][self.guardCol+1] == "#" or self.grid[self.guardRow][self.guardCol+1] == "O":
                self.turn()
            else:
                self.guardCol += 1

        return True
    

    def step(self):
        """
        Take a step and record the location and path
        """
        result = self.stepWithoutRecording()
        self.recordStep()
        return result


    def recordStep(self):
        self.path.append((self.guardRow, self.guardCol, self.direction))
        self.locations.add((self.guardRow, self.guardCol))
        self.grid[self.guardRow][self.guardCol] = self.direction


    def isLoop(self):
        while self.stepWithoutRecording():
            if (self.guardRow, self.guardCol, self.direction) in self.path:
                return True
            self.recordStep()
        return False
    

    def obstruct(self, row, col):
        self.grid[row][col] = "O"