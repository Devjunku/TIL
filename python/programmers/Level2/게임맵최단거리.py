from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(maps, n, m, visited):

    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny]:
                    continue
                if maps[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
    return visited


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited = bfs(maps, n, m, visited)

    if visited[n-1][m-1]:
        return visited[n-1][m-1]
    else:
        return -1



if __name__ == "__main__":
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))