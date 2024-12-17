from Block import Block
from typing import Set

class WideGrid:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].strip())*2

        self.grid = []
        self.blocks = []
        for row, line in enumerate(lines):
            gridLine = []
            for col, char in enumerate(line.strip()):
                if char == "#":
                    gridLine.append("#")
                    gridLine.append("#")
                elif char == ".":
                    gridLine.append(".")
                    gridLine.append(".")
                elif char == "O":
                    gridLine.append(".")
                    gridLine.append(".")
                    block = Block(row, col*2)
                    self.blocks.append(block)
                elif char == "@":
                    gridLine.append(".")
                    gridLine.append(".")
                if "@" in line:
                    self.rRow = row
                    self.rCol = line.index("@")*2
            self.grid.append("".join(gridLine))
            
            

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

        # Push stack is a list of blocks that will be pushed
        stack = self.getPushStack(direction, dRow, dCol)
        for block in stack:
            block.row += dRow
            block.col += dCol


    def getPushStack(self, direction, dRow, dCol) -> Set[Block]:
        pushStack = set()
        pushedCoords = set()

        # Maintain a set containing all the (row,col) coords that get pushed
        # It starts with the coord the robot is immediately trying to move to
        pushedCoords.add((self.rRow+dRow, self.rCol+dCol))

        # Iterate through the set of coords being pushed
        while len(pushedCoords) > 0:
            coord = pushedCoords.pop()
            
            # If trying to push a # then nothing moves
            if self.grid[coord[0]][coord[1]] == "#":
                return []
            
            # If the coord contains a block, add the block to the push stack
            for block in self.blocks:                
                if block.row == coord[0] and (block.col == coord[1] or block.col+1 == coord[1]):
                    pushStack.add(block)
                    pushed = block.getPushed(direction)
                    pushedCoords.update(pushed)
                    break

        # If we ended the loop normally then we didn't hit a wall, so can move the robot
        self.rRow += dRow
        self.rCol += dCol

        return pushStack
        


    def calcGPSSum(self):
        sum = 0
        for block in self.blocks:
            sum += 100*block.row + block.col
        return sum
    

    def print(self):
        printable = []
        for line in self.grid:
            printable.append(list(line))

        printable[self.rRow][self.rCol] = "@"

        for block in self.blocks:
            printable[block.row][block.col] = "["
            printable[block.row][block.col+1] = "]"

        for line in printable:
            print("".join(line))