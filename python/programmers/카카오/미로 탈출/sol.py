from heapq import heappop, heappush

INF = int(10**9)
d = [[INF for _ in range(1024)] for _ in range(1001)]
graph = [[] for _ in range(1001)]
rev_graph = [[] for _ in range(1001)]
trap_idx = [-1 for _ in range(1001)]


def bitmask(state, idx):
    return (1 << trap_idx[idx]) & state


def solution(n, start, end, roads, traps):

    for s, e, c in roads:
        graph[s].append((e, c))
        rev_graph[e].append((s, c))
    
    for i in range(len(traps)):
        trap_idx[traps[i]] = i
    
    pq = []
    d[start][0] = 0
    heappush(pq, (d[start][0], start, 0))

    # state가 의미하는 것은? → 어떤 노드를 방문했을 때 trap

    while pq:
        val, now, state = heappop(pq)
        
        if now == end: return val

        # TODO
        if d[now][state] != val: continue

        for nxt, dist in graph[now]:
            
            # TODO 현재와 다음 노드 둘 다 trap일 때
            # 방문했던 노드를 왔다 갔다 할 필요는 없으므로 q에 집어넣지 않기 위한 코드
            rev = 0
            if trap_idx[now] != -1 and bitmask(state, now): rev ^= 1
            if trap_idx[nxt] != -1 and bitmask(state, nxt): rev ^= 1
            
            if rev: continue

            nxt_state = state
            # TODO 다음 노드가 trap이라면, 
            if trap_idx[nxt] != -1:
                print("정방향 trap 전", bin(nxt_state)[2:])
                nxt_state ^= (1 << trap_idx[nxt])
                print("정방향 trap 후", bin(nxt_state)[2:])
            if d[nxt][nxt_state] > val + dist:
                d[nxt][nxt_state] = val + dist
                heappush(pq, (d[nxt][nxt_state], nxt, nxt_state))
        
        for nxt, dist in rev_graph[now]:
            rev = 0
            if trap_idx[now] != -1 and bitmask(state, now): rev ^= 1
            if trap_idx[nxt] != -1 and bitmask(state, nxt): rev ^= 1
            if not rev: continue

            nxt_state = state
            if trap_idx[nxt] != -1: nxt_state ^= (1 << trap_idx[nxt])
            if d[nxt][nxt_state] > val + dist:
                d[nxt][nxt_state] = val + dist
                heappush(pq, (d[nxt][nxt_state], nxt, nxt_state))


    return -1

if __name__ == "__main__":
    print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
    print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))