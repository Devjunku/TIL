# 틀린 풀이
# 가로 세로 500, 500인데 500*500*4의 시간복잡도가 필요 너무 많음
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())

mapping = [ list(map(int, input().split())) for _ in range(M) ]
visited = [ [1]*N for _ in range(M)]
visited[0][0] = 0
cnt = 0

def dfs(cx, cy):
    global cnt

    if cx == N-1 and cy == M-1:
        cnt += 1
        return

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if (mapping[ny][nx] < mapping[cy][cx]) and visited[ny][nx]:
                    visited[ny][nx] = -1
                    dfs(nx, ny)
                    visited[ny][nx] = 1

dfs(0, 0)
print(cnt)