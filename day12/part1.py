from Grid import Grid

def getPerimeter(region:set):
    edges = list()
    for plot in region:
        # Plot is a (row,col) tuple
        row = plot[0]
        col = plot[1]

        # Get the plot's edges
        plotEdges = []
        plotEdges.append((row,col,row,col+1))
        plotEdges.append((row+1,col,row+1,col+1))
        plotEdges.append((row,col,row+1,col))
        plotEdges.append((row,col+1,row+1,col+1))

        # Perimeter edges can appear only once
        for edge in plotEdges:
            if edge in edges:
                edges.remove(edge)
            else:
                edges.append(edge)

    return len(edges)

        
input = open("day12/input.txt", "r")
grid = Grid(input.read().splitlines())

grid.parseRegions()
score = 0
for region in grid.regions:
    area = len(region)
    perimeter = getPerimeter(region)
    score += area * perimeter

print("Score " + str(score))