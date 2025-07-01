import math

def printPowerSet(set,SetSize):
    powerSetSize = (int (math.pow(2, SetSize)))
    outer = 0
    inner = 0

    for outer in range(powerSetSize):
        for inner in range(SetSize):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = " ")
        print("")
size = int(input("Enter the size of the set: "))
set = []
for i in range(0,size):
    n = int(input("Enter element: "))
    set.append(n)

printPowerSet(set, len(set))
    