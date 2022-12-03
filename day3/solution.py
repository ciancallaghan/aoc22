import sys
import string

file = sys.argv[1]
alphabet = list(string.ascii_lowercase + string.ascii_uppercase)

with open(file, "r") as inputfile:
    common = []
    for line in inputfile:
        firsthalf = set(line[:len(line)//2])
        secondhalf = set(line[len(line)//2:])
        common.append(firsthalf.intersection(secondhalf).pop())
    for pos, let in enumerate(common):
        common[pos] = alphabet.index(let) + 1
    print(sum(common))

with open(file, "r") as inputfile:
    lines = inputfile.readlines()
    common = []
    for i in range(0, len(lines), 3):
        first = set(lines[i].strip())
        second = set(lines[i+1].strip())
        third = set(lines[i+2].strip())
        common.append(first.intersection(second).intersection(third).pop())
    for pos, let in enumerate(common):
        common[pos] = alphabet.index(let) + 1
    print(sum(common))
