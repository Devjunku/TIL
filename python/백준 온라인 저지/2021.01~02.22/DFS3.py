# 인접리스트 풀이
# https://underflow101.tistory.com/10 참고
from sys import stdin

def DFS(_graph, _start): # 인접리스트와 시작점 설정
    visit = [] # 방문 리스트
    stack = [_start] # 스택 리스트 처음 시작점은 초기값
    while stack: # stack이 없으면 중단
        node = stack.pop() # pop하고 그 값을 node에 저장
        if node not in visit: # 만약에 node가 방문 리스트에 없으면
            visit.append(node) # node를 방문 리스트에 추가
            if _graph[node] == None: # 그리고 인접 리스트의 node번째 원소가 None이라면
                return visit # 방문 리스트를 반환
                # 그렇지 않다면 인접 리스트의 node번째 원소를 -1씩 감소시키면서 순회
            for i in range(len(_graph[node])-1, -1, -1):
                stack.append(_graph[node][i]) # 순회 할 때마다 node번째 원소의 맨 끝 원소부터
    return visit    # 스택에 추가
    # 마지막으로 반환



N, M, V = map(int,stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(M):
    s, e = map(int,stdin.readline().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, len(graph)):
    graph[i].sort() # 정렬하고
for item in dfs(graph, V): # 출력
    print(item, end = ' ')



