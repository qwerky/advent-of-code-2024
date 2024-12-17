from Computer import Computer
from math import trunc

target = [2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0]

# By analysing the program, we can see it is simple.
# The program can be broken into 7 steps, which run in a loop.
#
# 1. 2,4 bst
#     b = a % 8
#     set b to a's remainder when divided by 8
#
# 2. 1,1 bxl
#     b = b XOR 1
#     flip the last bit of b
#
# 3. 7,5 cdv
#     c = trunc(a/(1 << b))
#     set c to a over 2 to the power b
#
# 4. 1,5 bxl
#     b = b XOR 5
#     flip some more bits in b
#
# 5. 4,2 bxc
#     b = b XOR c
#     flip some more bits in b
#
# 6. 5,5 out
#     output b % 8
#     The output step, gives us the remainder of b from 8
#
# 7. 0,3 adv
#     a = a/(8)
#     perform integer division on a by 8
#
# 8. 3,0 jnz
#     if a > 0 set instruction pointer to 0
#     
# Here are the facts:
# There are 7 steps, which repeat in a loop until a is less than 8
# b and c don't carry over each iteration; they are set fresh anew each loop based on the value of a
#
# With this knowledge, given a desired output value and a known final value for a, we can work backwards to find the possible values of a at the start of the loop.
# As we perform integer division, dividing a by 8, we know for a given end value of a the only possible start values are between 8a and 8a+7, which is a small enough
# number we can just check them all.
def getPossibleAValues(endA, desiredOutput):
    possbileAValues = []
    for startA in range(endA*8, (endA+1)*8):
        b = startA % 8
        b = b ^ 1
        c = trunc(startA/(1<<b))
        b = b ^ 5
        b = b ^ c
        output = b % 8
        if output == desiredOutput:
            possbileAValues.append(startA)
    return possbileAValues

# Now we can iterate through the target sequence backwards, performing a search for the possible A values at each step
solutions = set()
def buildStep(endA, step):
    desiredOutput = target[step]

    # For each candidate a value at this stage
    startAs = getPossibleAValues(endA, desiredOutput)
    if len(startAs) > 0 and step == 0:
        solutions.update(startAs)
    for a in startAs:
        buildStep(a, step-1)
        
# We know the final value of a must be zero in order for the program to terminate
buildStep(0, 15)

# Lets test each solution to make sure
for solution in solutions:
    puter = Computer(solution, 0, 0, target)
    puter.run()
    if puter.output == target:
        print(f"Found solution {solution}")
    else:
        print(f"Bad solution {solution}")