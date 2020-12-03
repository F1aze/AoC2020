input = open("../in/1.in", "r")

data = []

for line in input:
    data.append(int(line.strip()))
   
for i in data:
    for j in data:
        for k in data:
            if j+i+k == 2020:
                print(i*j*k)