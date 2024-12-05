import math


stage2 = False
orders = []
updates = []

file = "./day5.txt"
# file = "./testi.txt"

with open(file) as file:
    for line in file:
        if line == '\n':
            stage2 = True

        if not stage2:
            orders.append(line.strip().split("|"))

        if stage2:
            updates.append(line.strip().split(","))
file.close()


incorrets = []
corrects = []
for update in updates:
    correct = True
    temp_rules = []

    for i in range(0,len(update)):
        for order in orders:
            if order[0] == update[i] or order[1] == update[i]:
                temp_rules.append(order)


    for i in range(0,len(update)):

        for j in range(0,len(temp_rules)):

            if update[i] == temp_rules[j][1]:
                
                for k in range(i,len(update)):
                    if update[k] == temp_rules[j][0]:
                        correct = False

    if correct == True and update != ['']: corrects.append(update)
    elif update != ['']: incorrets.append(update)

total = 0
for update in corrects:
    i = math.floor(len(update)/2)
    total += int(update[i])

print(total)


def swap(list,a,b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    return list


for update in incorrets:
    temp_rules = []

    for i in range(0,len(update)):
        for order in orders:
            if order[0] == update[i] or order[1] == update[i]:
                temp_rules.append(order)


    for i in range(0,len(update)):

        for j in range(0,len(temp_rules)):

            if update[i] == temp_rules[j][1]:
                
                for k in range(i,len(update)):
                    if update[k] == temp_rules[j][0]:
                        swap(update,i,k)
    print(incorrets)


total = 0
for update in incorrets:
    i = math.floor(len(update)/2)
    total += int(update[i])

print(total)
