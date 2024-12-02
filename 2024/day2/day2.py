def sign(x : int) -> int:
    if x > 0: return 1
    if x < 0: return -1
    return 0

reports = []
bads = []
levels = []

with open("./day2.txt") as file:
    for line in file:
        reports.append(line)
file.close

total_safes = 0
for i in range(0, len(reports)):
    is_safe = True
    levels = reports[i].split(" ")

    change : int = int(levels[0]) - int(levels[1])
    direction = sign(change)

    for j in range(0, len(levels)-1):
        change : int = int(levels[j]) - int(levels[j+1])

        if (abs(change) > 3):
            is_safe = False
            break

        if (sign(change) == 0):
            is_safe = False
            break

        if (sign(change) != direction):
            is_safe = False
            break

    if (is_safe == True): 
        total_safes += 1
    else:
        bads.append(reports[i])

print("part1:", total_safes)


for i in range(0, len(bads)):
    levelsC = bads[i].split(" ")
    for k in range(0,len(levelsC)):
        is_safe = True
        levels = bads[i].split(" ")
        del levels[k]

        change : int = int(levels[0]) - int(levels[1])
        direction = sign(change)

        for j in range(0, len(levels)-1):
            change : int = int(levels[j]) - int(levels[j+1])

            if (abs(change) > 3):
                is_safe = False
                break

            if (sign(change) == 0):
                is_safe = False
                break

            if (sign(change) != direction):
                is_safe = False
                break

        if (is_safe == True):
            total_safes += 1
            break

print("part2:", total_safes)
