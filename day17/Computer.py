from math import trunc

class Computer:

    def __init__(self, a, b, c, program):
        self.a = a
        self.startA = a
        self.b = b
        self.c = c
        self.program = program
        self.instructionPointer = 0
        self.output = []


    def run(self):
        while self.instructionPointer < len(self.program) - 1:
            self.tick()
            

    def print(self):
        print(",".join(str(v) for v in self.output))
        print(f"a={self.a} b={self.b} c={self.c}")


    def tick(self):
        opcode = self.program[self.instructionPointer]
        operand = self.program[self.instructionPointer+1]
        return self.exec(opcode, operand)


    def exec(self, opcode:int, operand:int):
        match opcode:
            case 0:
                self.adv(operand)
            case 1:
                self.bxl(operand)
            case 2:
                self.bst(operand)
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc(operand)
            case 5:
                return self.out(operand)
            case 6:
                self.bdv(operand)
            case 7:
                self.cdv(operand)


    def combo(self, operand:int):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        elif operand == 7:
            raise RuntimeError("Reserved combo operand 7")
        raise RuntimeError("Unknown operand " + str(operand))


    def adv(self, operand:int):
        self.a = trunc(self.a/(1<<self.combo(operand)))
        self.instructionPointer += 2

    
    def bxl(self, operand:int):
        self.b = self.b ^ operand
        self.instructionPointer += 2
    

    def bst(self, operand:int):
        self.b = self.combo(operand) % 8
        self.instructionPointer += 2


    def jnz(self, operand:int):
        if self.a == 0:
            self.instructionPointer += 2
        else:
            self.instructionPointer = operand
        

    def bxc(self, operand:int):
        self.b = self.b ^ self.c
        self.instructionPointer += 2

    
    def out(self, operand:int):
        result = self.combo(operand) % 8
        self.output.append(result)
        self.instructionPointer += 2
        return result


    def bdv(self, operand:int):
        self.b = trunc(self.a/(1<<self.combo(operand)))
        self.instructionPointer += 2


    def cdv(self, operand:int):
        self.c = trunc(self.a/(1<<self.combo(operand)))
        self.instructionPointer += 2
