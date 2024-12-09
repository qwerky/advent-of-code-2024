input = open("day9/input.txt", "r")
line = input.read().splitlines()[0]

# Expand out the line
# 12345
# becomes
# 0..111....22222

# 2333133121414131402
# becomes
# 00...111...2...333.44.5555.6666.777.888899

disk = []
isFile = True
fileId = 0

for char in line:
    if isFile:
        text = [str(fileId)] * int(char)
        isFile = False
        fileId += 1
    else:
        text = ["."] * int(char)
        isFile = True

    disk.extend(text)


# Now compact the disk

# 0..111....22222
# becomes
# 022111222......

# 00...111...2...333.44.5555.6666.777.888899
# becomes
# 0099811188827773336446555566..............

left = 0
right = len(disk)-1

while (left < right):
    # move left forwards to the next free space
    while not disk[left] == ".":
        left += 1

    # move right backwards to find the next file
    while disk[right] == ".":
        right -= 1

    if left < right:
        disk[left] = disk[right]
        disk[right] = "."
        left += 1
        right -= 1


# Compute checksum
checksum = 0
for index, char in enumerate(disk):
    if char == ".":
        break
    checksum += index * int(char)

print(checksum)