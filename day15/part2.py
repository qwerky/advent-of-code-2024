from WideGrid import WideGrid

input = open("day15/input.txt", "r")
lines = input.read().splitlines()

gridMode = True
gridLines = []
pathLines = []
for line in lines:
    if len(line.strip()) > 1:
        if gridMode:
            gridLines.append(line)
        else:
            pathLines.append(line)
    else:
        gridMode = False

grid = WideGrid(gridLines)
for pathLine in pathLines:
    for step in pathLine:
        grid.step(step)

grid.print()

print(grid.calcGPSSum())
