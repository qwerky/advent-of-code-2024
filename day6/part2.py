import copy
from Grid import Grid

input = open("day6/input.txt", "r")
grid = Grid(input.readlines())

tempGrid = copy.deepcopy(grid)
while tempGrid.step():
    pass
path = tempGrid.path

obstructions = set()
# Step through the path backwards
while len(path) > 0:
    pos = path.pop()
    
    # if this isn't a crossing
    if pos not in path:
        tempGrid = copy.deepcopy(grid)
        tempGrid.obstruct(pos[0],pos[1])
        if tempGrid.isLoop():
            obstructions.add((pos[0],pos[1]))
            print("Found loop " + str(pos))
            #tempGrid.print()
print(len(obstructions))