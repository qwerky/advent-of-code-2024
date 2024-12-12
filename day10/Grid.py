class Grid:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].strip())

        self.grid = []
        for line in lines:
            self.grid.append(list(line.strip()))

        self.trails = set()
        self.pathCount = 0
        

    def walk(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == "0":
                    self.findTrails((row,col))

    
    def findTrails(self, start:tuple):
        locations = set()
        locations.add(start)
        for num in range(1, 10):
            locations = self.getNext(locations, str(num))
        
        for location in locations:
            self.trails.add((start[0], start[1], location[0], location[1]))


    # Given a set of locations and a number, find all
    # adjacent locations which are one value higher
    def getNext(self, locations:set, num):
        results = set()
        for location in locations:
            results.update(self.getAdjacent(location[0], location[1], num))
        return results


    # Returns coordinate tuples for each adjacent position with the value
    def getAdjacent(self, row, col, value):
        results = set()
        
        # Above?
        if row > 0 and self.grid[row-1][col] == value:
            results.add((row-1,col))

        # Below?
        if row < self.height-1 and self.grid[row+1][col] == value:
            results.add((row+1,col))

        # Left?
        if col > 0 and self.grid[row][col-1] == value:
            results.add((row,col-1))

        # Right?
        if col < self.width-1 and self.grid[row][col+1] == value:
            results.add((row,col+1))

        return results
        

    def getPaths(self, start:tuple):
        # Build a graph and count the number of paths from start -> end
        
        # First, build a graph as a map of one location to a set containing all the next locations
        graph = {}
        locations = set()
        locations.add(start)

        for num in range(1, 10):
            nextLocations = set()

            for location in locations:
                # Get the next steps and add them to the graph
                nextSteps = self.getAdjacent(location[0], location[1], str(num))
                graph[location] = nextSteps

                # Add all the steps to the locations to process in the next number
                nextLocations.update(nextSteps)
            
            locations = nextLocations.copy()

        for location in locations:
            graph[location] = set()
        return graph
    

    def countPaths(self, node:tuple, end:tuple, visited:dict, graph:dict, count:int) -> int:
       visited[node] = True
       
       if node == end:
           count += 1
       else:
           for next in graph[node]:
               if visited[next] == False:
                   count = self.countPaths(next, end, visited, graph, count)
       visited[node] = False
       return count
    