from Grid import Grid
from Robot import Robot

input = open("day14/input.txt", "r")
lines = input.read().splitlines()

#grid = Grid(11, 7)
grid = Grid(101, 103)
for line in lines:
    robot = Robot(line)
    grid.robots.append(robot)

for seconds in range(100):
    grid.step()

print(grid.score())
