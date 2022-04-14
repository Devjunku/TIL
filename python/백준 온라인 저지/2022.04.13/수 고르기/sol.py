import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = [int(input()) for _ in range(n)]
seq.sort()

left = 0
right = 0

ans = int(1e10)
while left <= right and right < n:

    if seq[right] - seq[left] < m:
        right += 1
    else:
        ans = min(seq[right] - seq[left], ans)
        left += 1
print(ans)