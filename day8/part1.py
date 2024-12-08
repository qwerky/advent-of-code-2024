from Grid import Grid
import itertools

input = open("day8/input.txt", "r")
lines = input.read().splitlines()

grid = Grid(len(lines[0]), len(lines))

# build map of antennas
for row in range(grid.height):
    for col in range(grid.width):
        frequency = lines[row][col]
        if not frequency == ".":
            grid.addAntenna(row, col, frequency)

# iterate antenna frequencies, adding nodes
for frequency in grid.antennaMap:
    locations = grid.antennaMap[frequency]
    for pair in itertools.combinations(locations, 2):
        # pair = ( (a1row,a1col), (a2row,a2col) )
        vOffset = pair[0][0] - pair[1][0]
        hOffset = pair[0][1] - pair[1][1]
        
        grid.addNode(pair[0][0] + vOffset, pair[0][1] + hOffset)
        grid.addNode(pair[1][0] - vOffset, pair[1][1] - hOffset)

print(len(grid.nodes))