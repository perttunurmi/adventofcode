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

total = 0
for i in range(0,len(data_l)):
    total += abs(data_l[i] - data_r[i])

print(total)
