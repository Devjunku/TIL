'''
간단한 다익스트라 알고리즘 구현 예시

진행 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'
하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차탐색) 해야한다.

간단한 다익스트라 알고리즘의 시간 복잡도는 O(V^2) [V: 노드의 갯수]이라 한다.
즉 노드의 갯수가 5000개 이상인 문제의 경우 간단한 다익스트라 알고리즘으로 문제를 풀이하는 것은 어렵다.
따라서 개선된 다익스트라 알고리즘을 이용해야 하는데, 이는 다음에..

#### 예시 문제 ####
 
1번 째 줄에 n과 m이 주어지며 n은 노드의 개수 m은 간선정보의 개수이다.
2번 째 줄에는 시작 노드가 주어진다.
이후
m개의 간선정보가 주어진다.

시작 노드부터 각 노드까지의 최단 거리를 구하시오.

##################

입력값
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력값
0
2
3
1
2
4
'''

# 데이터 입력 부분
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 다익스트라를 진행하기 위한 세팅
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

# 데이터 입력, graph부분에 추가해야함.
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 시작 노드는 인덱스, 도착 노드는 튜플 형태의 원소로 저장

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 인덱스 '초 기 값' 설정

    for i in range(1, n+1):
        # 방문하지도 않아야하고 최소값보다 작아야함.
        if distance[i] < min_value and not visited[i]: 
            min_value = distance[i]
            index = i
    
    return index


def dijkstra(start):
    # 시작 노드를 초기화 함
    distance[start] = 0 # 시작점은 거리가 0 이니까~
    visited[start] = True # 첫 시작 노드 방문 처리하고

    for j in graph[start]: # 시작 노드에서 도착 노드는 0번 인덱스 거리는 1번 인덱스에 있음 그리고 이는 튜플형태로 저장했었음
        distance[j[0]] = j[1] # 거리 리스트에 저장

    for i in range(n-1): # 시작 노드는 이미 처리했으니까. 남은 노드만 처리하자
        now = get_smallest_node()
        # 시작 노드는 처리되었으니까 이를 먼저 가장 거리가 짧은 노드의 번로를 반환하자.
        # 그리고 이를 방문처리하자
        visited[now] = True

        # 그리고 가장 거리가 짧은 노드가 현재의 노드의 위치이고
        # 거리를 누적했을 때 가장 짧은 아이를 저장하자.
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            # 현재 노드를 거처서 다른 노드로 이동할 때 거리가 짧은 경우를 캐치!
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 수행
dijkstra(start)

# 거리 행렬을 보았을 때 INF가 아니면
# 시작 노드부터 해당 도착 노드까지의
# 최단거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])