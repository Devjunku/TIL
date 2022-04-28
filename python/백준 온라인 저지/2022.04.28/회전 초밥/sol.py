import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

init_q = deque([])
for i in range(k):
    init_q.append(arr[i])

init_set = set(init_q)
answer = 0
if c not in init_set:
    answer += 1
answer += len(init_set)

for i in range(k, n+k):
    init_q.popleft()
    init_q.append(arr[i%n])
    init_set = set(init_q)
    if c in init_set:
        answer = max(len(init_set), answer)
    else:
        answer = max(len(init_set)+1, answer)

print(answer)