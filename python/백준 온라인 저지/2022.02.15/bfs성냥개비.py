import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

INT_MAX = sys.maxsize
dp_max = [0 for _ in range(101)]
dp_min = [INT_MAX for _ in range(101)]
count = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
initial = [[value, idx] for idx, value in enumerate(count)][1:]

for idx, value in enumerate(count):
    print(idx, value)


q = deque(initial)

while q:
    cnt, make = q.popleft()
    dp_min[cnt] = min(dp_min[cnt], make)

    if dp_min[cnt] != make: continue

    for i in range(10):
        if cnt + count[i] <= 100:
            q.append([cnt + count[i], int(str(make) + str(i))])

for _ in range(T):
    p = int(input())
    max_string = ""
    if p % 2 == 1:
        max_string = "7" + "1" * ((p-3) // 2)
    else:
        max_string = "1" * (p // 2)
    print(f"{dp_min[p]} {max_string}")