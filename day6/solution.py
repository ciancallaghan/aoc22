import sys

file = sys.argv[1]

with open(file, "r") as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        for i in range(3, len(line.strip())):
            marker = [line[i-3], line[i-2], line[i-1], line[i]]
            duplicates = [bit for bit in marker if marker.count(bit) > 1]
            if (len(duplicates) > 0):
                pass
            else:
                break
    print(i + 1)
    for line in lines:
        for i in range(13, len(line.strip())):
            message_marker = [line[i-j] for j in range(0, 14)]
            duplicates = [bit for bit in message_marker if message_marker.count(bit) > 1]
            if (len(duplicates) > 0):
                pass
            else:
                break
    print(i+1)
