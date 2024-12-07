from xmas import countXmas

input = open("day4/input.txt", "r")
grid = input.readlines()

height = len(grid)
width = len(grid[0])
print("height " + str(height) + ", width " + str(width))

count = 0
for row in range(1, height - 1):
    for col in range(1, width - 1):
        if grid[row][col] == "A":
            word1 = grid[row-1][col-1] + "A" + grid[row+1][col+1]
            word2 = grid[row-1][col+1] + "A" + grid[row+1][col-1]
            if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
                count += 1


print(count)