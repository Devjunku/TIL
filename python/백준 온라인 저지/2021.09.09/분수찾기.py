import sys
input = sys.stdin.readline

cnt = 1

n = int(input())
dy = 0
dx = 0
x, y  = 0, 0
d = (1, -1)
while cnt != n:
    x, y = x + d[0], y + d[1]
    if y < 0:
        dy += 1
        x, y = 0, dy
        d = (1, -1)
        cnt += 1
        continue
    elif x < 0:
        dx += 1
        x, y = dx, 0
        d = (-1, 1)
        cnt += 1
        continue
    else:
        cnt+=1


print(f"{x+1}/{y+1}")
