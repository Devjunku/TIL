import heapq
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

cus = []
items = []
for _ in range(n):
    customer, item_cnt = map(int, input().split())
    cus.append(customer)
    items.append(item_cnt)

counter = []
for i in range(k):
    heapq.heappush(counter, (0, i))

time_needed = [0] * k

finished = []
for i in range(n):
    t, x = heapq.heappop(counter)
    time_needed[x] += items[i]
    heapq.heappush(counter, (time_needed[x], x))
    finished.append((time_needed[x], -x, i))

print(sum(cus[t[2]] * (i+1) for i, t in enumerate(sorted(finished))))