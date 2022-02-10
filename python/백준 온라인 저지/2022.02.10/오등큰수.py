import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
F_value = {}

for i in range(n):
    try:
        F_value[arr[i]] += 1
    except:
        F_value[arr[i]] = 1

stack = [0]
answer = [-1 for _ in range(n)]

for i in range(n):
    print(f"stack : {stack}")
    while stack and F_value[arr[stack[-1]]] < F_value[arr[i]]:
        answer[stack[-1]] = arr[i]
        print(f"answer : {answer}")
        stack.pop()
    stack.append(i)

print(*answer)