import sys


'''
다익스트라

모든 지점의 거리를 무한대로 둔 다음에 시작 위치의 이동 비용을 계산하여
최소값을 갱신하며 나가는 알고리즘

어제 다익스트라 들었을 때 멘붕와서 재빨리 찾아봤는데, 사실 이 문제 다익스트라로 풀려고 하다가
BFS로 풀고 싶어서 그냥 BFS로 풀었다.

일반적인 BFS에서 살짝 조건을 더 붙인 문제인데
방향을 설정할 때 최소값만 저장해주는 방식이다.
최소값이 설정되면 queue로 저장해주고 그렇지 않으면 무시..

처음 다익스트라를 배울 때, 모든 거리를 INF로 설정하고 접근하는데,
이 문제도 접근할 때, 애초에 거리를 말도 안 되게 (10억) 설정해서 접근했기 때문에
개념을 어느 정도 활용했다고 할 수 있으나, 아직 다익스트라 코드를 혼자 구현하진 못한다.
'''


sys.stdin = open('sample_input.txt')

from collections import deque

INF = 1e9

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    global coordinate, dist
    dist[0][0] = 0

    while coordinate:
        x, y = coordinate.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                default_cost = 1

                if map_data[nx][ny] > map_data[x][y]:
                    default_cost += (map_data[nx][ny] - map_data[x][y])

                if dist[nx][ny] > dist[x][y] + default_cost:
                     dist[nx][ny] = dist[x][y] + default_cost    
                     coordinate.append((nx, ny))


T = int(input())

for t in range(1, T+1):
    N = int(input())
    map_data = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    coordinate = deque()
    coordinate.append((0, 0))

    bfs()

    print(f'#{t} {dist[N-1][N-1]}')