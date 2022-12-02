import os
import sys

file = sys.argv[1]
opplist = ["A", "B", "C"]
melist = ["X", "Y", "Z"]

with open(file, "r") as inputfile:
    scorelist1 = []
    for line in inputfile:
        score = 0
        opp = line.split()[0]
        me = line.split()[1]
        game = opplist.index(opp) - melist.index(me)
        if (game == 0):
            score += 3
            score += melist.index(me) + 1
        elif (game == 1 or game == -2):
            score += melist.index(me) + 1
        elif (game == -1 or game == 2):
            score += 6
            score += melist.index(me) + 1
        print(game)
        scorelist1.append(score)

with open(file, "r") as inputfile:
    scorelist2 = []
    for line in inputfile:
        score = 0
        opp = line.split()[0]
        me = line.split()[1]
        if (me == "X"):
            score += 0
            score += opplist.index((opplist[(opplist.index(opp) - 1)])) + 1
        elif (me == "Y"):
            score += 3
            score += opplist.index((opplist[(opplist.index(opp))])) + 1
        elif (me == "Z"):
            score += 6
            score += opplist.index(opplist[(opplist.index(opp) + 1 - 3)]) + 1
        scorelist2.append(score)

print(sum(scorelist1))
print(sum(scorelist2))
