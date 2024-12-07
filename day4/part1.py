from xmas import countXmas

input = open("day4/input.txt", "r")
grid = input.readlines()

height = len(grid)
width = len(grid[0])
print("height " + str(height) + ", width " + str(width))

count = 0
for row in range(height):
    for col in range(width):
        print("row " + str(row) + ", col " + str(col))
        words = []
        
        # Right
        words.append(grid[row][col:col+4])
        
        # Left
        if col > 2:
            words.append(grid[row][col] + grid[row][col-1] + grid[row][col-2] + grid[row][col-3])

        # Up
        if row > 2:
            words.append(grid[row][col] + grid[row-1][col] + grid[row-2][col] + grid[row-3][col])

        # Down
        if row + 3 < height:
            words.append(grid[row][col] + grid[row+1][col] + grid[row+2][col] + grid[row+3][col])
        
        # Up & left
        if row > 2 and col > 2:
            words.append(grid[row][col] + grid[row-1][col-1] + grid[row-2][col-2] + grid[row-3][col-3])

        # Up & right
        if row > 2 and col + 3 < width:
            words.append(grid[row][col] + grid[row-1][col+1] + grid[row-2][col+2] + grid[row-3][col+3])

        # Down & right
        if row + 3 < height and col + 3 < width:
            words.append(grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] + grid[row+3][col+3])

        # Down & left
        if row + 3 < height and col > 2:
            words.append(grid[row][col] + grid[row+1][col-1] + grid[row+2][col-2] + grid[row+3][col-3])

        count += countXmas(words)

print(count)