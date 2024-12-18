from Grid import Grid

grid = Grid(71)
input = open("day18/input.txt", "r")
lines = input.read().splitlines()

count = 0
path = None
for line in lines:
    col = int(line.split(",")[0])
    row = int(line.split(",")[1])
    grid.grid[col][row] = "#"
    count += 1

    if path is not None and (col, row) not in path:
        continue

    if count > 1024:
        path = grid.dijkstra()
        if len(path) == 1:
            print(f"No path for {col},{row}")
            break