import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().split())

idx = []
weight = []

for _ in range(n):
    i, w = map(int, input().split())
    idx.append(i)
    weight.append(w)

counter = []
for i in range(k):
    heappush(counter, (0, i))

time_need = [0] * k

finish = []
for i in range(n):
    t, x = heappop(counter)
    time_need[x] += weight[i]
    heappush(counter, (time_need[x], x))
    finish.append((time_need[x], -x, i))

print(sum(idx[t[2]] * (i+1) for i, t in enumerate(sorted(finish))))