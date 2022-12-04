import sys

file = sys.argv[1]
duplicates = 0
overlaps = 0

with open(file, "r") as inputfile:
    for line in inputfile:
        first = line.strip().split(",")[0].split("-")
        second = line.strip().split(",")[1].split("-")
        firstset = set([i for i in range(int(first[0]), int(first[1])+1)])
        secondset = set([i for i in range(int(second[0]), int(second[1])+1)])

        if (firstset.issubset(secondset) or secondset.issubset(firstset)):
            duplicates += 1

        if (len(firstset.intersection(secondset)) > 0):
            overlaps += 1

print(duplicates, overlaps)
