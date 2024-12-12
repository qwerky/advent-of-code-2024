from Grid import Grid
import itertools

def getPerimeter(region:set):
    edges = []
    for plot in region:
        # Plot is a (row,col) tuple
        row = plot[0]
        col = plot[1]

        # An edge is defined as a tuple with (startRow, startCol, endRow, endCol, side) where side is t, b, l or r

        # Get the plot's top, bottom, left and right edges
        plotEdges = []
        plotEdges.append((row,col,row,col+1, "t"))
        plotEdges.append((row+1,col,row+1,col+1, "b"))
        plotEdges.append((row,col,row+1,col, "l"))
        plotEdges.append((row,col+1,row+1,col+1, "r"))

        # If the opposite edge has been found, its an internal edge so not part of the perimeter
        for edge in plotEdges:
            opp = (edge[0], edge[1], edge[2], edge[3], opposite(edge[4]))
            if opp in edges:
                edges.remove(opp)
            else:
                edges.append(edge)

    return edges


def opposite(side):
    if side == "t":
        return "b"
    elif side == "b":
        return "t"
    elif side == "l":
        return "r"
    elif side == "r":
        return "l"
    else:
        raise RuntimeError("Unknown side")

def getSides(perimeter:set):
    newPerimeter = set()
    while len(perimeter) > 0:
        # An edge is a tuple with (startRow, startCol, endRow, endCol, side)
        # Go through the perimeter, examining each edge
        # For each edge, find ones that join together and therefore can be merged
        thisEdge = perimeter.pop()
        merged = False
        for edge in perimeter:
            # If they are inline
            if (thisEdge[0] == thisEdge[2] and edge[0] == edge[2] and thisEdge[0] == edge[0]) or (thisEdge[1] == thisEdge[3] and edge[1] == edge[3] and thisEdge[1] == edge[1]):
                # If they are adjoining
                if (thisEdge[2],thisEdge[3]) == (edge[0],edge[1]) or (thisEdge[0],thisEdge[1]) == (edge[2],edge[3]):
                    # If both facing same way
                    if thisEdge[4] == edge[4]:

                        # We can merge these edges into a new, bigger edge
                        startRow = min(thisEdge[0], edge[0])
                        startCol = min(thisEdge[1], edge[1])
                        endRow = max(thisEdge[2], edge[2])
                        endCol = max(thisEdge[3], edge[3])
                        newEdge = (startRow, startCol, endRow, endCol, edge[4])
                        perimeter.remove(edge)
                        perimeter.append(newEdge)
                        merged = True
                        break
        
        if not merged:
            newPerimeter.add(thisEdge)

    return newPerimeter

        
input = open("day12/input.txt", "r")
grid = Grid(input.read().splitlines())

grid.parseRegions()
score = 0
for region in grid.regions:
    area = len(region)
    perimeter = getPerimeter(region)
    sides = getSides(perimeter)
    score += area * len(sides)

print("Score " + str(score))