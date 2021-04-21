'''
#### 개선된 다익스트라 알고리즘 ####

😑 대부분의 코드가 heapq 모듈을 사용하고 있어서 한 번 따라해보았습니다.

'개선된 다익스트라'는 '간단한 다익스트라'와 별 차이가 없지만, 이를 '우선순위 큐'로 구현한 것이라 합니다.
따라서 시간 복잡도가 현저히 줄어드는 효과를 볼 수 있습니다.

**시간복잡도**
V: 노드의 개수
E: 간선의 개수
간단한 다익스트라: O(V^2)
개선된 다익스트라: O(E*logV)

**참고 사항**
우선순위 큐 구현 방식에 따른 시간 복잡도

**리스트로 구현**
삽입 시간: O(1)
삭제 시간: O(N)

**Heapq로 구현**
삽입 시간: O(logN)
삭제 시간: O(logN)


- 개선된 다익스트라 알고리즘 -
Key Point: '최단 거리가 가장 짧은 노드'를 선택하는 과정을 다익스트라 함수 안에서 '우선순위 큐'로 구현

#### 예시는 앞선 것과 동일함 ####
'''

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 다익스트라를 진행하기 위한 세팅
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 데이터 입력, graph부분에 추가해야함.
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 시작 노드는 인덱스, 도착 노드, 거리를 튜플 형태의 원소로 저장


def Dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))

    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

Dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])