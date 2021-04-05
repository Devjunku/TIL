import sys

sys.stdin = open('input.txt')

T = 10

def bfs(n):
    pass


for t in range(1, T+1):
    # 정점 총 수, 간선의 총 수, 공통 조상 찾기 위한 정점 번호
    V, E, n1, n2 = map(int, input().split()) # 정점번호 중 누굴 택해서 돌려야할까?
    # 방문했는지? 안했으면 셀거임
    visited = [0 for _ in range(V+1)]
    left = [0 for _ in range(V+1)]
    right = [0 for _ in range(V+1)]
    # 트리 정점 정보 받기
    node_list = list(map(int, input().split()))

    # 간선 정보 입력
    for x, y in node_list:
        print(x, y)

    # 찾으면 끝임




