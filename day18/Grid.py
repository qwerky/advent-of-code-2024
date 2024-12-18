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

        Q = set()
        dist = {}
        prev = {}
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[col][row] == ".":
                    v = (col,row)
                    dist[v] = self.big
                    prev[v] = None
                    Q.add(v)
        
        dist[start] = 0

        while len(Q) > 0:
            min = self.big
            for u in Q:
                if dist[u] < min:
                    min = dist[u]
                    nearest = u
            if nearest == end:
                break
            Q.remove(nearest)
            for v in self.getNeighbours(nearest, Q):
                alt = dist[nearest] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = nearest

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
        if up in Q:
            neighbours.add(up)
        down = (col, row+1)
        if down in Q:
            neighbours.add(down)
        left = (col-1, row)
        if left in Q:
            neighbours.add(left)
        right = (col+1, row)
        if right in Q:
            neighbours.add(right)
        
        return neighbours



    def print(self):
        for line in self.grid:
            print("".join(line))