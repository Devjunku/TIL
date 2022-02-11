import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ren_line = []

for _ in range(k):
    ren_line.append(int(input()))

left, right = 1, max(ren_line)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(k):
        cnt += ren_line[i] // mid
    
    if cnt < n:
        right = mid - 1
    else:
        left = mid + 1

if left == 1:
    print(left)
else:
    print(left-1)