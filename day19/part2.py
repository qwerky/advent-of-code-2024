
def countPossible(line:str):
    if line in cache:
        return cache[line]
    
    possible = 0
    for design in designs:
        if line == design:
            possible += 1
        elif line.startswith(design):
            trimmedLine = line[len(design):]
            possible += countPossible(trimmedLine)
    
    cache[line] = possible
    return possible


input = open("day19/input.txt", "r")
lines = input.read().splitlines()

designs = lines[0].split(", ")

count = 0
for row in range(2, len(lines)):

    line = lines[row]
    print("Checking " + line)

    cache = {}
    solutions = countPossible(line)
    if solutions > 0:
        print(f"{line} has {solutions} solutions ")
    else:
        print(line + " has no solutions")
    count += solutions

print(count)