import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
INF = int(1e9)
peoples = set()

for _ in range(M):
    one, two = map(int, input().split())
    graph[one].append((1, two))
    graph[two].append((1, one))
    peoples.add(one)
    peoples.add(two)

peoples = list(peoples)
peoples.sort()

friends = [[0 for _ in range(N)] for _ in range(N)]

def dijkstra(start):
    
    init_dist = [INF for _ in range(N+1)]
    init_dist[start] = 0
    HQ = []
    heappush(HQ, (0, start))

    while HQ:
        cost, now = heappop(HQ)

        if init_dist[now] < cost: continue

        for add_cost, nxt in graph[now]:
            new_cost = cost + add_cost

            if init_dist[nxt] > new_cost:
                init_dist[nxt] = new_cost
                heappush(HQ, (init_dist[nxt], nxt))
    
    return init_dist

number = INF
answer = -1

for i in range(1, N+1):
    summm = sum(dijkstra(i)[1:])
    if number > summm:
        answer = i
        number = summm

print(answer)   