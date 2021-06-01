from heapq import heappop, heappush
import sys

INF = int(sys.maxsize)

def dijkstra(s, distance, room):

    q = []
    heappush(q, (0, s))

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for cost, node in room[now]:
            cost += dist
            if distance[node] > cost:
                distance[node] = cost
                heappush(q, (cost, node))
    
    return distance


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    room = [[] for _ in range(N+1)]

    for m in range(M):
        a, b, c = map(int, input().split())
        room[a].append((c, b))
        room[b].append((c, a))

    K = int(input())
    K_loc = list(map(int, input().split()))

    # 이 부분이 문제임... 다시 좀 뜯어보자
    res_list = [0] * (N+1)
    for j in K_loc:
        distance = [INF] * (N+1)
        res = dijkstra(j, distance, room)
        for i in range(1, N+1):
            res_list[i] += res[i]

    answer = res_list.index(min(res_list))
    print(answer)

## 오랜만에 다익스트라 문제를 풀었는데, 진짜 오랜만에 만져보는 최단거리 문제..
## 하하.. 복습좀 철저히 해야겠당..ㅠㅠ