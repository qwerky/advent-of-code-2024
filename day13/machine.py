class Machine:

    def __init__(self, a, b, p):
        self.ax = int(a.split(", ")[0].split("+")[1])
        self.ay = int(a.split(", ")[1].split("+")[1])
        
        self.bx = int(b.split(", ")[0].split("+")[1])
        self.by = int(b.split(", ")[1].split("+")[1])

        self.px = int(p.split(", ")[0].split("=")[1])
        self.py = int(p.split(", ")[1].split("=")[1])