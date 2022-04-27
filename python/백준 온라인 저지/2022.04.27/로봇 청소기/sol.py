import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy, d = map(int, input().split())

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[sx][sy] = True
answer = 1

while True:
    print(sx, sy)
    flag = 0
    for _ in range(4):
        nx, ny = sx + dx[(d+3)%4], sy + dy[(d+3)%4]
        d = (d+3)%4
        if (0 <= nx < n and 0 <= ny < m) and arr[nx][ny] == 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                answer += 1
                sx, sy = nx, ny
                flag = 1
                break

    if flag == 0:
        if arr[sx-dx[d]][sy-dy[d]] == 1:
            print(answer)
            break
        else:
            sx, sy = sx-dx[d], sy-dy[d]
