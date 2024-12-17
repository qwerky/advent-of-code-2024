input = open("day16/input.txt", "r")
lines = input.readlines()

grid = []
Q = set()       # Work queue
dist = {}       # Distance map
prev = {}       # Used for path building
path = []
finish = []

def opposite(direction):
    match direction:
        case ">":
            return "<"
        case "<":
            return ">"
        case "^":
            return "v"
        case "v":
            return "^"


def dijkstra(end):
    while len(Q) > 0:
        
        if len(Q) % 100 == 0:
            print(f"There are {len(Q)} node left to process")

        u = getNearest()
        if u[0] == end[0] and u[1] == end[1]:
            finish.append(u)
            break
        Q.remove(u)
        for v in getNeighbours(u):
            alt = dist[u] + 1
            
            # If have to turn to get from v to u then we add 1000
            if not u[2] == v[2]:
                if u[2] == opposite(v[2]):
                    alt += 2000
                else:
                    alt += 1000
            
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    u = finish[0]
    while u in prev:
        path.append(u)
        u = prev[u]



def getNeighbours(u):
    row = u[0]
    col = u[1]
    neighbours = set()
    
    up = (row-1, col, "^")
    if up in Q:
        neighbours.add(up)
    down = (row+1, col, "v")
    if down in Q:
        neighbours.add(down)
    left = (row, col-1, "<")
    if left in Q:
        neighbours.add(left)
    right = (row, col+1, ">")
    if right in Q:
        neighbours.add(right)
    
    return neighbours


def getNearest():
    min = 99999999999
    for v in Q:
        if dist[v] < min:
            min = dist[v]
            nearest = v
    return nearest


for row, line in enumerate(lines):
    grid.append(line)
    for col, char in enumerate(line):
        if char == "S":
            start = (row, col, ">")
            for c in "<>^v":
                Q.add((row, col, c))
                dist[(row, col, c)] = 99999999999
                prev[(row, col, c)] = None
        elif char == "E":
            end = (row, col)
            for c in "<>^v":
                Q.add((row, col, c))
                dist[(row, col, c)] = 99999999999
                prev[(row, col, c)] = None
        elif char == ".":
            for c in "<>^v":
                dist[(row, col, c)] = 99999999999
                prev[(row, col, c)] = None
                Q.add((row, col, c))


dist[start] = 0
dijkstra(end)
print(path)
print(dist[finish[0]])