from pandas import DataFrame
from sys import stdin

c, r = map(int,stdin.readline().rstrip().split())

N = int(stdin.readline().rstrip())

arr = [[0 for _ in range(c+1)] for _ in range(r+1)]

loca = []
for _ in range(N+1):
    c1, r1 = map(int,stdin.readline().rstrip().split())

    if c1 == 1:
        arr[r][r1] = 1
        loca.append([r1, r])
    elif c1 == 2:
        arr[0][r1] = 1
        loca.append([r1, 0])
    elif c1 == 3:
        arr[r-r1][0] = 1
        loca.append([0, r-r1])
    else:
        arr[r-r1][c] = 1
        loca.append([c, r-r1])

dongg = loca.pop()
res_distan = 0
for n in range(N):
    x1, y1 = loca[n][0], loca[n][1]
    x2, y2 = dongg[0], dongg[1]
    # print(x1, y1)
    # print(x2, y2)
    
    if x1 == x2 or y1 == y2:
        res = abs((x1 + y1) - (x2 + y2))
    else:
        if (x1 + y1 + x2 + y2) < (2*c + 2*r - x1 - y1 - x2 -y2):
            res = (x1 + y1 + x2 + y2)
        else:
            res = (2*c + 2*r - x1 - y1- x2 -y2)
        
    res_distan += res
    
print(res_distan)

    # print(x1 + y1)
    # print(c-x1 + r-y1)
    # print(x2 + y2)
    # print(c-x2 + r-y2)

    


    
        

    

# 0,0 을 가느냐,  c,r로 가느냐



