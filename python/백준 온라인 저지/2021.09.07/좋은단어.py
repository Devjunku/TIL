import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    string = input().strip()
    stack = [string[0]]
    for i in range(1, len(string)):
        if stack:
            if string[i] == stack[-1]: stack.pop()
            else: stack.append(string[i])
        else: stack.append(string[i]) 
    if not stack: cnt += 1

print(cnt)