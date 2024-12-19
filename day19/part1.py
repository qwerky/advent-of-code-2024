

def isPossible(line:str):
    for design in designs:
        if line == design:
            return True
        elif line.startswith(design):
            trimmedLine = line[len(design):]
            if isPossible(trimmedLine):
                return True
    return False



input = open("day19/input.txt", "r")
lines = input.read().splitlines()

designs = lines[0].split(", ")

count = 0
for row in range(2, len(lines)):
    if isPossible(lines[row]):
        print(lines[row] + " is possible")
        count += 1

print(count)