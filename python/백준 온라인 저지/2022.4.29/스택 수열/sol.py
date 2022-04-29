import sys
from collections import deque
input = sys.stdin.readline

q = deque([])

n = int(input())
start = 1
for _ in range(n):
    q.append(int(input()))

stack = []
answer = []

i = 1
while True:
    if not q:
        break
    if not stack:
        stack.append(i)
        answer.append("+")
        i += 1
    else:
        if stack[-1] == q[0]:
            stack.pop()
            answer.append("-")
            q.popleft()
            continue
        else:
            if i < n+1:
                stack.append(i)
                answer.append("+")
                i += 1
            else:
                break


if stack:
    print("NO")
else:
    for a in answer:
        print(a)


    


