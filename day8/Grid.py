class Grid:

    def __init__(self, width, height):
        self.antennaMap = {}
        self.nodes = set()
        self.width = width
        self.height = height


    def addAntenna(self, row, col, frequency):
        if frequency in self.antennaMap:
            self.antennaMap[frequency].append((row,col))
        else:
            freqList = []
            freqList.append((row,col))
            self.antennaMap[frequency] = freqList


    def addNode(self, row, col):
        if row < 0 or col < 0:
            return False
        if row >= self.height or col >= self.width:
            return False
        self.nodes.add((row,col))
        return True