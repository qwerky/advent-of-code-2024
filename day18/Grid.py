from Hq import Hq

class Grid:

    def __init__(self, size):
        self.height = size
        self.width = size
        self.big = 99999999

        self.grid = []
        for row in range(size):
            self.grid.append(["."]*size)
            
            
    def dijkstra(self):
        start = (0,0)
        end = (self.width-1, self.height-1)
        dist = {}
        prev = {}
        
        Q = Hq()
        dist[start] = 0
        Q.add(start, 0)

        for row in range(self.height):
            for col in range(self.width):
                if self.grid[col][row] == ".":
                    v = (col,row)
                    if not v == start:
                        dist[v] = self.big
                        prev[v] = None
                        Q.add(v, self.big)
        
        

        while Q.size() > 0:
            nearest = Q.pop()
            if nearest == end:
                break
            for v in self.getNeighbours(nearest, Q):
                alt = dist[nearest] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = nearest
                    Q.update(v, alt)

        path = []
        node = end
        while node in prev:
            path.append(node)
            node = prev[node]
        
        return path


    def getNeighbours(self, u, Q):
        col = u[0]
        row = u[1]
        neighbours = set()
        
        up = (col, row-1)
        if Q.contains(up):
            neighbours.add(up)
        down = (col, row+1)
        if Q.contains(down):
            neighbours.add(down)
        left = (col-1, row)
        if Q.contains(left):
            neighbours.add(left)
        right = (col+1, row)
        if Q.contains(right):
            neighbours.add(right)
        
        return neighbours



    def print(self):
        for line in self.grid:
            print("".join(line))