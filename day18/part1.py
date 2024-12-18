from Grid import Grid

grid = Grid(71)
input = open("day18/input.txt", "r")
lines = input.read().splitlines()

count = 0
for line in lines:
    if count == 1024:
        break
    row = int(line.split(",")[0])
    col = int(line.split(",")[1])
    grid.grid[col][row] = "#"
    count += 1

grid.print()
path = grid.dijkstra()
print(len(path))