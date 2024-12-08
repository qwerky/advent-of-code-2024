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
        vStep = pair[0][0] - pair[1][0]
        hStep = pair[0][1] - pair[1][1]
        
        # start at the first antenna in the pair
        # add nodes, increasing the position with v and h steps until we go out of bounds
        row = pair[0][0]
        col = pair[0][1]
        while grid.addNode(row, col):
            row += vStep
            col += hStep

        # now at the second antenna in the pair
        # add nodes, decreasing the position with v and h steps until we go out of bounds
        row = pair[1][0]
        col = pair[1][1]
        while grid.addNode(row, col):
            row -= vStep
            col -= hStep

print(len(grid.nodes))