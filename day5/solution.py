import sys

file = sys.argv[1]

# stack1 = ["Z", "N"]
# stack2 = ["M", "C", "D"]
# stack3 = ["P"]
# stacks = [stack1, stack2, stack3]
stack1 = ["F", "T", "C", "L", "R", "P", "G", "Q"]
stack2 = ["N", "Q", "H", "W", "R", "F", "S", "J"]
stack3 = ["F", "B", "H", "W", "P", "M", "Q"]
stack4 = ["V", "S", "T", "D", "F"]
stack5 = ["Q", "L", "D", "W", "V", "F", "Z"]
stack6 = ["Z", "C", "L", "S"]
stack7 = ["Z", "B", "M", "V", "D", "F"]
stack8 = ["T", "J", "B"]
stack9 = ["Q", "N", "B", "G", "L", "S", "P", "H"]
stacks = [stack1, stack2, stack3, stack4, stack5,
          stack6, stack7, stack8, stack9]

with open(file, "r") as inputfile:
    lines = inputfile.readlines()
    lines = lines[lines.index("\n")+1:]

    for line in lines:
        line = line.split()
        number = int(line[1])
        from_stack = int(line[3]) - 1
        to_stack = int(line[5]) - 1
        mover = []
        for i in range(number):
            # Problem 1
            # stacks[to_stack].append(stacks[from_stack].pop())
            mover.append(stacks[from_stack].pop())
        mover.reverse()
        for item in mover:
            stacks[to_stack].append(item)

res = []
for stack in stacks:
    res.append(stack.pop())

print(res)
