# test1 - 1
# test2 - 2
# test3 - 4
# test4 - 3
# test5 - 36


from Grid import Grid

input = open("day10/input.txt", "r")
grid = Grid(input.read().splitlines())

grid.walk()            
print(str(len(grid.trails)) + " trails")
