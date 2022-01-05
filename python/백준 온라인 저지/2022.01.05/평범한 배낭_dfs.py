# dfs 풀이 근데 틀림

import sys

n, k = map(int, sys.stdin.readline().strip().split())

w_list = []
v_list = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().strip().split())
    w_list.append(w)
    v_list.append(v)


visited = [False for _ in range(n)]
answer = 0

def dfs(weight, value):
    global answer


    if weight > k:
        return
    else:
        answer = max(answer, value)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(weight + w_list[i], value + v_list[i])
            visited[i] = False

dfs(0, 0)
print(answer)