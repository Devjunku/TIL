from collections import deque

n, m  = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, inpit())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y)) # 미로 시작점은 0, 0이므로 일단 추가

    while queue: # 큐가 빌 때까지 지속
        x, y = queue.popleft() # 일단 방문 했으니 pop하고
        for i in range(4): 
            nx = x + dx[i] # 갈 곳을 정함
            ny = x + dy[i] 
            if nx < 0 or ny < 0 o nx >= n or ny >= n: # 미로의 범위에 넘어선다면
                continue # 볼 필요없고 넘어감
            if graph[nx][ny] == 0: # 0이면, 벽이니까 다시 볼 필요 없음
                continue
            if graph[nx][ny] == 1: # 벽이 아닌 길이라면
                graph[nx][ny] = graph[x][y] + 1 # 첫 시작점에 1을 더한 상태로 nx, ny 를 업데이트
                queue.append((nx, ny)) # 그리고 진행했다는 의미이므로 추가시킴
                                       # 이러한 방식을 4번 시행하여 한칸씩 이동할 때 마다
                                       # 모두 append() 하게됨. 즉 이동이 확실하게 된 부분에서 시작
                                       # 끝나면 그래프의 각 원소는 모두 시작지점부터까지의 거리가 계산되어
                                       # 기록됨. 
    return graph[x][y]

print(bfs(0,0))