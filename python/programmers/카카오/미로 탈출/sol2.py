from heapq import heappop, heappush

INF = int(10**9)
d = [[INF for _ in range(1024)] for _ in range(1001)]
graph = [[] for _ in range(1001)]
rev_graph = [[] for _ in range(1001)]
trap_idx = [-1 for _ in range(1001)]

def bitmask(state, idx):
    return (1 << trap_idx[idx]) & state


def solution(n, start, end, roads, traps):
    
    for s, e, v in roads:
        graph[s].append((e, v))
        rev_graph[e].append((s, v))
    
    for i in range(len(traps)):
        trap_idx[traps[i]] = i
    
    pq = []
    d[start][0] = 0
    heappush(pq, (d[start][0], start, 0))

    while pq:

        val, now, state = heappop(pq)
        if now == end: return val
        if d[now][state] != val: continue

        for nxt, dist in graph[now]:
            rev = 0
            if trap_idx[now] != -1 and bitmask(state, now): rev ^= 1
            if trap_idx[nxt] != -1 and bitmask(state, nxt): rev ^= 1
            if rev: continue

            nxt_state = state
            if trap_idx[nxt] != -1: nxt_state ^= (1 << trap_idx[nxt])
            if d[nxt][nxt_state] > dist + val:
                d[nxt][nxt_state] = dist + val
                heappush(pq, (d[nxt][nxt_state], nxt, nxt_state))

        for nxt, dist in rev_graph[now]:
            rev = 0
            if trap_idx[now] != -1 and bitmask(state, now): rev ^= 1
            if trap_idx[nxt] != -1 and bitmask(state, nxt): rev ^= 1
            if not rev: continue

            nxt_state = state
            if trap_idx[nxt] != -1: nxt_state ^= (1 << trap_idx[nxt])
            if d[nxt][nxt_state] > dist + val:
                d[nxt][nxt_state] = dist + val
                heappush(pq, (d[nxt][nxt_state], nxt, nxt_state))

    return -1

if __name__ == "__main__":
    print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
    print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))