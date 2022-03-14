import sys
input = sys.stdin.readline

n = int(input())
top_list = list(map(int, input().split()))
answer = [0 for _ in range(n)]

stack = []

for i in range(n):
    while stack:
        if top_list[i] < stack[-1][0]:
            answer[i] = stack[-1][1]
            break
        else:
            stack.pop()
    stack.append((top_list[i], i+1))

print(*answer)