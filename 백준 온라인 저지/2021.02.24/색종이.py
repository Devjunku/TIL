arr = [[0 for _ in range(102)] for _ in range(102)]

from sys import stdin

N = int(stdin.readline().rstrip())

data = []
for _ in range(N):
    data.append(list(map(int,stdin.readline().rstrip().split())))

data = data[::-1]

real_area = []
for i in range(len(data)):
    x1 = data[i][0]
    y1 = data[i][1]
    x2 = data[i][0] + data[i][2]-1
    y2 = data[i][1] + data[i][3]-1

    area = 0
    for j in range(x1, x2+1):
        for k in range(y1, y2+1):
            arr[j][k] += 1

            if arr[j][k] == 1:
                area += 1
    
    real_area.append(area)

for i in range(len(real_area)-1, -1, -1):
    print(real_area[i])
