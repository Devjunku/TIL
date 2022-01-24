from collections import deque
n = int(input())

def que(n):

    queue = deque([(n, 0)])
    while queue:
        number, cnt = queue.popleft()
        if number == 1:
            return cnt
        queue.append((number-1, cnt+1))
        if number % 3 == 0:
            queue.append((number//3, cnt+1))
            continue
        if number % 2 == 0:
            queue.append((number//2, cnt+1))
              
print(que(n))