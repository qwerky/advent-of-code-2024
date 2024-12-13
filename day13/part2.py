from machine import Machine
import math

input = open("day13/input.txt", "r")
lines = input.read().splitlines()

totalCost = 0
for i in range(0, len(lines), 4):
    a = lines[i]
    b = lines[i+1]
    prize = lines[i+2]

    m = Machine(a[10:], b[10:], prize[7:])
    m.px += 10000000000000
    m.py += 10000000000000

    # This can be solved by thinking of two straight lines.
    # Line A starts at the origin and progresses as button A is pressed.
    # Line B starts from some point on line A and crosses the location of the prize.
    # If we can work out the intersection of A and B, we can work out how many times
    # each button was pressed.
    #
    #       |               
    #       |               P          
    #       |               B        
    #       |              B     
    #     y |              BAA
    #       |           AAB
    #       |        AAA  B
    #       |     AAA    B
    #       |  AAA       B
    #       AAA-----------------------------
    #                      x
    #

    # Line A starts at origin and ends at the first point past px
    x1 = 0
    y1 = 0
    x2 = m.ax * math.ceil(m.px/m.ax)
    y2 = m.ay * math.ceil(m.px/m.ax)

    # Line B ends at origin and starts at first point below x axis
    x3 = m.px
    y3 = m.py
    x4 = m.px - m.bx * math.ceil(m.py/m.by)
    y4 = m.py - m.by * math.ceil(m.py/m.by)

    # Line intersection formula - I had to look this up
    # It is also carefully crafted to only use integer operations as
    # earlier code with floats appeared to lose precision
    ixNumerator = (x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)
    ixDenom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    iyNumerator = (x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)
    iYDenom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if ixNumerator % ixDenom == 0 and iyNumerator % iYDenom == 0:
        # Intersection is at integer coords
        ix = ixNumerator//ixDenom
        iy = iyNumerator//iYDenom
    else:
        continue

    # If the intersection is on a location we can get to by pressing A
    if ix % m.ax == 0 and iy % m.ay == 0:
        aPresses = ix//m.ax
        bPresses = (m.px - ix)//m.bx
        totalCost += 3*aPresses + bPresses

print(totalCost)