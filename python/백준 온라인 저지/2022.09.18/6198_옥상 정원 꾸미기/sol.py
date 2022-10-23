import sys
input = sys.stdin.readline

n = int(input())

buildings = [int(input()) for _ in range(n)]
stack = []

answer = 0

for i in range(n-1, 0, -1):
    for j in range(n-i, -1, -1):
        if not stack: break
        print(stack, answer)
        if buildings[i] <= stack[j]: break
        answer += 1
    stack.append(buildings[i])
