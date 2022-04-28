from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

belt = deque(list(map(int, input().split())))
robot = deque([0 for _ in range(n)])
level = 0

def confirm(): return False if belt.count(0) >= k else True


while confirm():
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1
        robot[-1] = 0
    
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    level += 1

print(level)