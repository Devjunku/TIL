import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
p = {}
rank = {}
edge = []

for _ in range(M):
    s, e, c = map(int, input().split())
    edge.append([s, e, c])

edge.sort(key=lambda x: x[2])

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u1, u2):
    root1 = find(u1)
    root2 = find(u2)

    if rank[root1] > rank[root2]:
        p[root2] = root1
    else:
        p[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
    
for i in range(1, N+1):
    p[i] = i
    rank[i] = i

res = 0
for e in edge:
    start, end, cost = e
    if find(start) != find(end):
        union(start, end)
        res += cost

print(res)

