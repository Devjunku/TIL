from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

user_num = []
weight = []

for _ in range(n):
    i, w = map(int, input().split())
    user_num.append(i)
    weight.append(w)

time = [0] * k

pq = []

for i in range(k):
    heappush(pq, (0, i))

finish = []
for i in range(n):
    t, idx = heappop(pq)
    time[idx] += weight[i]
    heappush(pq, (time[idx], idx))
    finish.append((time[idx], -idx, i))

print(sum(user_num[t[2]] * (i+1) for i, t in enumerate(sorted(finish))))
