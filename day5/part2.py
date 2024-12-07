from pagechecker import checkValid
from pagechecker import fixIt

input = open("day5/input.txt", "r")

ruleMap = {}
updates = []

ruleParsingMode = True
for line in input.readlines():
    if line == "\n":
        ruleParsingMode = False
    else:
        if ruleParsingMode:
            first = line.split("|")[0]
            second = line.split("|")[1].strip()
            if ruleMap.get(first) == None:
                ruleMap[first] = [second]
            else:
                ruleMap[first].append(second)
        else:
            updates.append(line.strip())
input.close()

score = 0
for line in updates:
    pages = line.split(",")
    if not checkValid(pages, ruleMap):
        correctPages = fixIt(pages, ruleMap)
        middle = correctPages[int((len(correctPages)-1)/2)]
        score += int(middle)

print(score)