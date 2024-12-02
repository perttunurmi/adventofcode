data_l = []
data_r = []

with open("./day1.txt") as file:
    for line in file:
        a = line.split('   ')
        data_l.append(int(a[0]))
        data_r.append(int(a[1]))
file.close

data_l.sort()
data_r.sort()

total_distance = 0
for i in range(0,len(data_l)):
    total_distance += abs(data_l[i] - data_r[i])

print("part1: ", total_distance)


similarity_score : int = 0
for i in range(0, len(data_l)):
    apperases_in_right : int = 0
    for j in range(0, len(data_r)):
        if (data_l[i] == data_r[j]):
            apperases_in_right += 1
    similarity_score += data_l[i] * apperases_in_right 

print("part2: ", similarity_score)
