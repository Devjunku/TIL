from collections import deque
from operator import le
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))

updown = deque([0 for _ in range(n)])

def comfirm(): return False if belt.count(0) >= k else True

level = 0

while comfirm():

    belt.rotate(1)
    updown.rotate(1)
    updown[-1] = 0

    if sum(updown):
        for i in range(n-2, -1, -1):
            if updown[i] == 1 and updown[i+1] == 0 and belt[i+1] > 0:
                updown[i] = 0
                updown[i+1] = 1
                belt[i+1] -= 1
        updown[-1] = 0

    if updown[0] == 0 and belt[0] > 0:
        updown[0] = 1
        belt[0] -= 1
    
    level += 1

print(level)