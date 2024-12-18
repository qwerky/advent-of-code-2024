from Grid import Grid

grid = Grid(71)
input = open("day18/input.txt", "r")
lines = input.read().splitlines()

count = 0
for line in lines:
    col = int(line.split(",")[0])
    row = int(line.split(",")[1])
    grid.grid[col][row] = "#"
    count += 1

    if count > 1024:
        path = grid.dijkstra()
        if len(path) > 1:
            if count % 100 == 0:
                print(f"OK after {count} blocks, path is {len(path)-1}")
        else:
            print(f"No path for {col},{row}")
            break