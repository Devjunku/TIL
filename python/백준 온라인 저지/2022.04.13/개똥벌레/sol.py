import sys
input = sys.stdin.readline

n, h = map(int, input().split())

arr = [int(input()) for _ in range(n)]

height = [0 for _ in range(h)]

for i in range(n):
    if i % 2 == 0:
        print(height[-1:-3])
        # height[-1:-arr[i]-1] += 1
    else:
        height[0:arr[i]] += 1

print(height)
