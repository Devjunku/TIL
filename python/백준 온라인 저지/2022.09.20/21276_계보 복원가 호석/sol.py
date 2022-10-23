import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
people = set(input().split())
child = {person: [] for person in people}
edge = {person: [] for person in people}
indegree = {person: 0 for person in people}
father = []

m = int(input())

for _ in range(m):
    a, b = input().split()
    indegree[a] += 1
    edge[b].append(a)

q = deque()
for person in people:
    if not indegree[person]:
        q.append(person)
        father.append(person)

while q:
    node = q.popleft()
    for nxt_node in edge[node]:
        indegree[nxt_node] -= 1
        if not indegree[nxt_node]:
            q.append(nxt_node)
            child[node].append(nxt_node)

print(len(father))
print(*sorted(father))

for name in sorted(list(people)):
    print_str = name + " " + str(len(child[name]))
    if len(child[name]) != 0:
        print_str += (" " + " ".join(sorted(child[name])))
    print(print_str)