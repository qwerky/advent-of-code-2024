class Robot:

    def __init__(self, line):
        # p=0,4 v=3,-3
        parts = line.split()                   #  [p=0,4][v=3,-3]
        
        p = parts[0].split("=")[1].split(",")  #  [0][4]
        self.x = int(p[0])
        self.y = int(p[1])

        v = parts[1].split("=")[1].split(",")  #  [3][-3]
        self.vx = int(v[0])
        self.vy = int(v[1])


    def step(self, val, width, height):
        self.x += self.vx * val
        self.y += self.vy * val

        if self.x < 0:
            self.x += width
        elif self.x >= width:
            self.x -= width

        if self.y < 0:
            self.y += height
        elif self.y >= height:
            self.y -= height