# xmas
pattern = r'XMAS'
total = 0

lines = []
with open("./day4.txt") as file:
    for line in file:
        lines.append(line)
file.close


for i in range(0,len(lines)):


    for j in range(0,len(lines[i])):

        if (j+3 < len(lines[i])): # horizontal oikealle
            if (lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3] == "XMAS"): total += 1

        if (j-3 >= 0): # horizontal vasemmalle
            if (lines[i][j] + lines[i][j-1] + lines[i][j-2] + lines[i][j-3] == "XMAS"): total += 1



        if (i+3 < len(lines)): # vert alaspäin
            if (lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == "XMAS"): total += 1

        if (i-3 >= 0): # vert ylöspäin 
            if (lines[i][j] + lines[i-1][j] + lines[i-2][j] + lines[i-3][j] == "XMAS"): total += 1



        if (i+3 < len(lines) and j+3 < len(lines[i])): # diagonal oikealle alas
            if (lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == "XMAS"): total += 1

        if (i+3 < len(lines) and j-3 >= 0): # diagonal vasemmalle alas
            if (lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] == "XMAS"): total += 1

        if (i-3 >= 0 and j-3 >= 0): # diagonal vasemmalle ylos
            if (lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3] == "XMAS"): total += 1

        if (i-3 >= 0 and j+3 < len(lines[i])): # diagonal oikealle ylos
            if (lines[i][j] + lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3] == "XMAS"): total += 1

print(total)



# x-mas
total = 0

lines = []
with open("./day4.txt") as file:
    for line in file:
        lines.append(line)
file.close


for i in range(0,len(lines)):

    for j in range(0,len(lines)):

        if lines[i][j] == "A":
            if 0 < i and i + 1 < len(lines) and 0 < j and j + 1 < len(lines):
                if lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1] == "MAS" or lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1] == "SAM":
                    if lines[i+1][j-1] + lines[i][j] + lines[i-1][j+1] == "MAS" or lines[i+1][j-1] + lines[i][j] + lines[i-1][j+1] == "SAM":
                        total += 1

print(total)
