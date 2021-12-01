from collections import defaultdict, deque

def bfs(i, s, e):
    q = deque()
    q.append(i)
    dist[i] = 1
    curr = 0
    cnt = 1

    while q:
        cpoint = q.popleft()

        for next_point in graph[cpoint]:
            if cpoint == s and next_point == e or cpoint == e and next_point == s:
                continue




def solution(n, wires):
    answer = 1000000
    graph = defaultdict(list)
    for wire in wires:
        s, e = wire
        graph[s].append(e)
        graph[e].append(s)
    
    for wire in wires:
        dist = [0] * (n+1)
        s, e = wire
        temp = []
        for i in range(1, 1+n):
            if not dist[i]:
                max_dist = bfs(i, s, e)
                temp.append(max_dict)
        answer = min(answer, abs(temp[0] - temp[1]))

    return answer