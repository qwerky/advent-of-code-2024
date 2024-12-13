from machine import Machine
import timeit

input = open("day13/input.txt", "r")
lines = input.read().splitlines()

totalCost = 0
for i in range(0, len(lines), 4):
    a = lines[i]
    b = lines[i+1]
    prize = lines[i+2]

    m = Machine(a[10:], b[10:], prize[7:])
    cost = 99999999

    for a in range(101):
        for b in range(101):
            x = a*m.ax + b*m.bx
            y = a*m.ay + b*m.by
            if (x,y) == (m.px,m.py):
                cost = min(cost, 3*a + b)

    if not cost == 99999999:
        totalCost += cost

print(totalCost)
