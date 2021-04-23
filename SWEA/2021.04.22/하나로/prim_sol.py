import sys

sys.stdin = open('input.txt')

def extract_min(visit, distance):
    min_key = float('inf')
    min_idx = 0
    for i in range(N):
        if not visit[i] and distance[i] < min_key:
            min_idx = i
            min_key = distance[i]
    return min_idx
 
 
def prim(s):
    key = [float('inf')] * N
    key[s] = 0
    mst = [0] * N
    for _ in range(N - 1):  # N - 1개 선택
        u = extract_min(mst, key)
        mst[u] = 1
 
        for v in range(N):
            if not mst[v]:
                key[v] = min(key[v], adj[u][v])
 
    return sum(key[1:])
 
 
for tc in range(1, 1 + int(input())):
    N = int(input())  # N : 섬의 개수
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # adj[i][j] : i와 j 사이의 가중치
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    E = float(input())  # E : 세율 실수
    # 환경부담금: 환경부담세율(E) * (해저터널 길이(L) **2)
    for i in range(N):
        for j in range(i + 1, N):
            adj[i][j] = ((x[i] - x[j]) ** 2) + ((y[i] - y[j]) ** 2)
            adj[j][i] = adj[i][j]
    print('#%d' % tc, round(prim(0) * E))