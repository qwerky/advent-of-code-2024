from  math import floor, ceil

class Grid:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.steps = 0

        self.robots = []


    def step(self, val):
        self.steps += val
        for robot in self.robots:
            robot.step(val, self.width, self.height)


    def score(self):
        return self.count(0, floor(self.width/2)-1, 0, floor(self.height/2)-1)  \
            * self.count(ceil(self.width/2), self.width-1, 0, floor(self.height/2)-1)   \
            * self.count(0, floor(self.width/2)-1, ceil(self.height/2), self.height-1)   \
            * self.count(ceil(self.width/2), self.width-1, ceil(self.height/2), self.height-1)
    

    def count(self, xFrom, xTo, yFrom, yTo):
        count = 0
        for robot in self.robots:
            if xFrom <= robot.x <= xTo and yFrom <= robot.y <= yTo:
                count += 1
        return count
    
    def suspicious(self):
        q1 = self.count(0, floor(self.width/2)-1, 0, floor(self.height/2)-1)
        q2 = self.count(ceil(self.width/2), self.width-1, 0, floor(self.height/2)-1)
        q3 = self.count(0, floor(self.width/2)-1, ceil(self.height/2), self.height-1)
        q4 = self.count(ceil(self.width/2), self.width-1, ceil(self.height/2), self.height-1)

        expected = len(self.robots)/4

        c1 = self.chi2(q1, expected)
        c2 = self.chi2(q2, expected)
        c3 = self.chi2(q3, expected)
        c4 = self.chi2(q4, expected)

        return c1 + c2 + c3 + c4


    def chi2(self, observed, expected):
        return ((observed - expected)**2)/expected
    