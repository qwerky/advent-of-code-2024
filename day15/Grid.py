class Grid:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].strip())

        self.grid = []
        for row, line in enumerate(lines):
            self.grid.append(list(line.strip()))
            if "@" in line:
                self.rRow = row
                self.rCol = line.index("@")
            
            
            
    def step(self, direction:str):
        if direction == ">":
            dRow = 0
            dCol = 1
        elif direction == "<":
            dRow = 0
            dCol = -1
        elif direction == "^":
            dRow = -1
            dCol = 0
        elif direction == "v":
            dRow = 1
            dCol = 0

        # Push stack is a list of (row,col) tuples, starting with the robot
        # and ending with the first free space in the given direction.
        stack = self.getPushStack(dRow, dCol)

        # If the stack is empty then no free space was found, so can't push
        if len(stack) == 0:
            return
        else:
            self.rCol += dCol
            self.rRow += dRow

        prev = stack.pop()
        while len(stack) > 0:
            this = stack.pop()
            self.grid[prev[0]][prev[1]] = this[2]
            prev = this
        self.grid[this[0]][this[1]] = "."
        

    def getPushStack(self, dRow, dCol):
        stack = []
        row = self.rRow
        col = self.rCol
        stack.append((row, col, "@"))
        while True:
            row += dRow
            col += dCol
            char = self.grid[row][col]
            stack.append((row, col, char))
            if char == ".":
                return stack
            elif char == "#":
                return []
    


    def calcGPSSum(self):
        sum = 0
        for rowIndex, row in enumerate(self.grid):
            for colIndex, char in enumerate(row):
                if char == "O":
                    sum += rowIndex * 100 + colIndex
        return sum
    

    def print(self):
        for line in self.grid:
            print(line)
        print(f"Robot at ({self.rRow},{self.rCol})")