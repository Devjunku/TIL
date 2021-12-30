from collections import deque
import sys

n = int(input())
q = deque([])

for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
   
    if len(order) == 2:
        if order[0] == "push_back":
            q.append(order[1])
        elif order[0] == "push_front":
            q.appendleft(order[1])
    else:
        if order[0] == "pop_front":
            if q:
                ele = q.popleft()
                print(ele)
            else:
                print(-1)
        elif order[0] == "pop_back":
            if q:
                ele = q.pop()
                print(ele)
            else:
                print(-1)
        elif order[0] == "size":
            print(len(q))
        elif order[0] == "empty":
            if q:
                print(0)
            else:
                print(1)
        elif order[0] == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif order[0] == "back":
            if q:
                print(q[-1])
            else:
                print(-1)