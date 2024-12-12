class Grid:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].strip())

        self.grid = []
        for line in lines:
            self.grid.append(list(line.strip()))

        self.regions = []


    # Region is a tuple with (char, area, perimeter)
    def parseRegions(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                c = self.grid[row][col]
                if c.isupper():
                    region = self.buildRegion(row, col)
                    self.regions.append(region)


    # Build a region starting at the row,col
    def buildRegion(self, row:int, col:int):
        region = set()
        c = self.grid[row][col]

        toProcess = set()
        toProcess.add((row,col))

        while len(toProcess) > 0:
            plot = toProcess.pop()
            region.add(plot)
            self.grid[plot[0]][plot[1]] = c.lower()
            adjacent = self.getAdjacent(plot[0], plot[1], c)
            toProcess.update(adjacent)
            
        return region


    # Returns a set of coordinate tuples for points next to the given row,col that contain value c
    def getAdjacent(self, row:int, col:int, c:str):
        results = set()
        
        # Above?
        if row > 0 and self.grid[row-1][col] == c:
            results.add((row-1,col))

        # Below?
        if row < self.height-1 and self.grid[row+1][col] == c:
            results.add((row+1,col))

        # Left?
        if col > 0 and self.grid[row][col-1] == c:
            results.add((row,col-1))

        # Right?
        if col < self.width-1 and self.grid[row][col+1] == c:
            results.add((row,col+1))

        return results
    