from sys import stdin


arr = [[0 for _ in range(101)] for _ in range(101)]

arr_1 = []
area = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            if arr[j][k] == 0:
                arr[j][k] += 1
                area += 1
            
print(area)




