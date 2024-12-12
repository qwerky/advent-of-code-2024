# test2 - 2
# test3 - 13
# test4 - 3
# test7 - 227
# test8 - 81


from Grid import Grid

input = open("day10/input.txt", "r")
grid = Grid(input.read().splitlines())

count = 0
for row in range(grid.height):
    for col in range(grid.width):
        if grid.grid[row][col] == "0":
            start = (row,col)
            graph = grid.getPaths(start)
          
            # Do a DFS from start to end on the graph
            visited = graph.copy()
            for v in visited:
                visited[v] = False
            count += grid.countPaths(start, visited, graph, 0)

print("Total score " + str(count))
