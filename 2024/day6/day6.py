import numpy as np
import copy

file = "./day6.txt"
# file = "./test.txt"

lines_const = []
lines = []
with open(file) as file:
    for line in file:
        lines_const.append(list(line))
file.close

lines = copy.deepcopy(lines_const)

# print(lines)

guard_x_y = np.array([])
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == "^":
            guard_x_y = np.array([i, j])

# print(guard_x_y)
guard_on_the_map = True
current_direction = [-1, 0]
route = []

i = guard_x_y[0]
j = guard_x_y[1]
dir_x = current_direction[1]
dir_y = current_direction[0]
while (guard_on_the_map):
    lines[i][j] = "X"

    if i + dir_y < 0 or i + dir_y >= len(lines):
        break
    if j + dir_x < 0 or j + dir_x >= len(lines):
        break

    if lines[i+dir_y][j+dir_x] == "." or lines[i+dir_y][j+dir_x] == "X":
        i = i + dir_y
        j = j + dir_x

    if 0 <= i + dir_y < len(lines) and 0 <= j + dir_x < len(lines):
        if lines[i+dir_y][j+dir_x] == "#":

            if dir_y == -1 and dir_x == 0:
                dir_y = 0
                dir_x = 1
            elif dir_y == 0 and dir_x == 1:
                dir_y = 1
                dir_x = 0
            elif dir_y == 1 and dir_x == 0:
                dir_y = 0
                dir_x = -1
            elif dir_y == 0 and dir_x == -1:
                dir_y = -1
                dir_x = 0

for line in lines:
    print(line)

total = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == "X":
            total += 1
print(total)


loops = 0
for k in range(0, len(lines_const)):
    for o in range(0, len(lines_const)):
        lines = copy.deepcopy(lines_const)

        if lines[k][o] != "^":
            lines[k][o] = "#"

        i = guard_x_y[0]
        j = guard_x_y[1]

        dir_x = current_direction[1]
        dir_y = current_direction[0]

        temp_list = []
        stupid_counter = 0

        print(k, o)

        while (guard_on_the_map):
            lines[i][j] = "X"

            temp_list.append([i, j, dir_y, dir_x])

            if stupid_counter % 1000 == 0:
                if temp_list.count(temp_list[stupid_counter]) > 2:
                    loops += 1
                    break

            if i + dir_y < 0 or i + dir_y >= len(lines):
                break
            if j + dir_x < 0 or j + dir_x >= len(lines):
                break

            if lines[i+dir_y][j+dir_x] == "." or lines[i+dir_y][j+dir_x] == "X":
                i = i + dir_y
                j = j + dir_x

            if 0 <= i + dir_y < len(lines) and 0 <= j + dir_x < len(lines):
                if lines[i+dir_y][j+dir_x] == "#":

                    if dir_y == -1 and dir_x == 0:
                        dir_y = 0
                        dir_x = 1
                    elif dir_y == 0 and dir_x == 1:
                        dir_y = 1
                        dir_x = 0
                    elif dir_y == 1 and dir_x == 0:
                        dir_y = 0
                        dir_x = -1
                    elif dir_y == 0 and dir_x == -1:
                        dir_y = -1
                        dir_x = 0
            stupid_counter += 1

print(loops)
