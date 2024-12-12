# test2 - 2
# test3 - 13
# test4 - 3
# test7 - 227
# test8 - 81


from Grid import Grid

input = open("day10/input.txt", "r")
grid = Grid(input.read().splitlines())

grid.walk()            
count = 0
for trail in grid.trails:
    start = (trail[0],trail[1])
    graph = grid.getPaths(start)

    end = (trail[2],trail[3])
    
     # Do a DFS from start to end on the graph
    visited = graph.copy()
    for v in visited:
        visited[v] = False
    count += grid.countPaths(start, end, visited, graph, 0)

print("Total score " + str(count))
