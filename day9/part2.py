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
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..

fileEnd = len(disk) - 1
fileStart = len(disk) - 1
while (fileId > 0):
    fileId -= 1

    # Find end index of this file
    while not disk[fileEnd] == str(fileId):
        fileEnd -= 1

    # Find start index of this file
    fileStart = fileEnd
    while disk[fileStart-1] == str(fileId):
        fileStart -= 1

    fileLength = 1 + fileEnd - fileStart
    print("file: " + str(fileId) + " length:" + str(fileLength))

    # Find first place in disk it can go
    # This loop can take a while and we call it 9999 times. Maybe better to store
    # disk segments as a list of tuples (fileId, length) instead of a list of blocks
    # which should make finding a free space a lot quicker
    for i in range(fileStart):
        segment = disk[i:i+fileLength]
        if len(segment) == fileLength and all(c == "." for c in segment):
            # Write the file
            for j in range(fileLength):
                disk[i+j] = str(fileId)
                disk[fileStart+j] = "."
            break

# Compute checksum
checksum = 0
for index, char in enumerate(disk):
    if not char == ".":
        checksum += index * int(char)

print(checksum)