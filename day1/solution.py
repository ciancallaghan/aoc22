import os
import sys

file = sys.argv[1]
calories = 0
callist = []

with open(file, "r") as inputfile:
    for line in inputfile:
        if (line == "\n"):
            callist.append(calories)
            calories = 0
        else:
            calories = calories + int(line)

callist.sort()
print(callist[-1])
print(callist[-1] + callist[-2] + callist[-3])
