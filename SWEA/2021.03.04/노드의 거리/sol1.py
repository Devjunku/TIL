import sys

sys.stdin = open('sample_input.txt')

# queue 하나로 어떻게 해보려고 했지만,
# 하나의 queue인해 업데이트 되는 노드들을
# 한번에 처리한 후 cnt를 세어야하는 번거로움이 존재
# 그러니까. 한번에 queue에 삽입되는 애들은 stack으로 만든 후
# 이걸 queue에 한번에 삽입하면서
# cnt를 세어주면 queue의 너비 증가 횟수를 세어줄 수 있음.
# 그래서 지속적으로 너비가 증갈 할 때마다 한 번에 업데이트 해줄 stack이 필요하고
# queue를 다 소비할 때까지 stack을 모으다가
# queue를 다 소비하면, stack에 있는걸 queue에 다시 넣어주어
# 그 다음 레벨의 너비를 탐색할 수 있게끔
# 조정해야함.
def BFS(adj_list, start, end):
    queue = [start]
    cnt = 1 # 우선 무조건 노드간 거리는 1일테니 초기값을 지정
    while queue: # queue로 돌릴건데
        stack = []  # 여기서 빈 stack을 만들고
        while queue: # 이제 여기서
            u = queue.pop(0) # queue를 앞에서 하나씩 꺼내면서
            visited[u] = 1 # 방문처리
            for v in adj_list[u]: # 인접리스트의 원소를 꺼내면서
                if v == end: # 만약에 목적지면
                    return cnt # 바로 cnt로 출력하고
                if visited[v]: # 그렇지 않고 방문했었으면
                    continue # 그냥 지나가야함
                stack.append(v) # 이 둘 모두에 해당이 안되면 stack에 기록하고
                visited[v] = 1 # 방문하지 않았으므로 방문기록을 함
        cnt += 1  # 안쪽 while구문을 다 돌면 queue가 빈 공간이 되므로 한차례의 너비는 다 계산
        queue = stack # 이제 모았던 stack을 queue에 다시 할당
    return 0 # 다 돌았는데, 목적지에 도착하지 않았다는 이야기이므로 0을 출력


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]
    visited = [ 0 for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)

    start, end = map(int, input().split())
    print('#{} {}'.format(t, BFS(adj_list, start, end)))