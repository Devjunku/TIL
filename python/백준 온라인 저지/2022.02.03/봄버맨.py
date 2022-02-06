import sys
from copy import deepcopy
from pprint import pprint
input = sys.stdin.readline

r, c, n = map(int, input().split())
answer = []
timer = [[[0, "empty"] for _ in range(c)] for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 초기
arr = [list(input().strip()) for _ in range(r)]
answer.append(deepcopy(arr))
# pprint(answer)
# 1초 후
for i in range(r):
    for j in range(c):
        if arr[i][j] == "O":
            timer[i][j][0] += 1
            timer[i][j][1] = "bomb"
answer.append(deepcopy(arr))

# 2초 후
for i in range(r):
    for j in range(c):
        if arr[i][j] == ".":
            timer[i][j][0] += 1
            timer[i][j][1] = "bomb"
            arr[i][j] = "O"
        else:
            timer[i][j][0] += 1
answer.append(deepcopy(arr))
# 3초 후
for i in range(r):
    for j in range(c):
        timer[i][j][0] += 1

for i in range(r):
    for j in range(c):
        if timer[i][j][0] == 3:
            arr[i][j] = "."
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    arr[nx][ny] = "."
answer.append(deepcopy(arr))

# 4초 후
for i in range(r):
    for j in range(c):
        arr[i][j] = "O"
answer.append(deepcopy(arr))

pprint(answer)

# for ele in answer[n % 5]:
#     print(*ele)