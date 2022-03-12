import sys
input = sys.stdin.readline

target = int(input())
ans = abs(100 - target)
M = int(input())

if M:
    broken = set(input().split())
else:
    broken = set()

for N in range(1000000):
    for number in str(N):
        if number in broken:
            break
    else:
        ans = min(ans, len(str(N)) + abs(N - target))

print(ans)