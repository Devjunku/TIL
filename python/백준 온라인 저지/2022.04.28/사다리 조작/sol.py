import sys
input =  sys.stdin.readline

def check():

    for i in range(n):
        y = i
        for j in range(h):
            if graph[j][y]:
                y += 1
            elif y > 0 and graph[j][y-1]:
                y -= 1

        if y != i:
            return False
    
    return True


def dfs(cnt, x, y):
    global answer

    if answer <= cnt:
        return
    
    if check():
        answer = min(answer, cnt)
        return
    
    if cnt == 3:
        return

    for i in range(x, h):
        k = y if i == x else 0

        for j in range(k, n-1):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0

n, m, h = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

answer = 4
dfs(0, 0, 0)
print(answer if answer <= 3 else -1)
