from Grid import Grid

input = open("day6/input.txt", "r")
grid = Grid(input.readlines())

while grid.step():
    pass

print(len(grid.locations))
print("loop? " + str(grid.isLoop()))