import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

r = [-1] * (n+1)
l = [-1] * (n+1)
visited = [[] for _ in range(n+1)]
parent = [-1] * (n+1)

for _ in range(n):
    p, left, right = map(int, input().split())
    l[p] = left
    r[p] = right
    if left != -1:
        parent[left] = p
    if right != -1:
        parent[right] = p

root = n
def find_root(node):
    global root

    if parent[node] == -1:
        root = node
        return
    else:
        find_root(parent[node])

idx = 1
def curcuit(node, start):
    global idx

    if l[node] != -1:
        curcuit(l[node], start+1)
    
    visited[start].append(idx)
    idx += 1

    if r[node] != -1:
        curcuit(r[node], start+1)

find_root(1)
curcuit(root, 1)

level = 1
width = 1
for i, v in enumerate(visited):
    if not v: continue
    if v[-1] - v[0] + 1 > width:
        width = v[-1] - v[0] + 1
        level = i

print(level, width)