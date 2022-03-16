from collections import deque
from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline
n, m, circle = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]
sx, sy = 0, 0
ex, ey = n-1, m-1

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while sx < ex and sy < ey:
    num = circle % (2 * ((ex-sx) + (ey-sy)))
    # print(num)
    direct = 0
    r = sx
    c = sy
    q1 = deque([])
    
    while True:

        q1.append((r, c))

        r += d[direct%4][0]
        c += d[direct%4][1]

        if r == ex and c == sy:
            direct += 1
        elif r == sx and c == ey:
            direct += 1
        elif r == ex and c == ey:
            direct += 1
        elif r == sx and c == sy:
            break

    q2 = deepcopy(q1)

    for _ in range(num):
        element = q1.pop()
        q1.appendleft(element)
    
    # print(q1)
    # print(q2)

    for i1, i2 in zip(q1, q2):
        answer[i2[0]][i2[1]] = arr[i1[0]][i1[1]]

    sx += 1
    sy += 1
    ex -= 1
    ey -= 1


for i in range(n):
    print(*answer[i])