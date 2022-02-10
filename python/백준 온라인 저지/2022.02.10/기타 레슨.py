import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)

while start <= end:
    mid = (start+end) // 2

    cnt = 0
    pt = 0
    for i in range(n):
        if pt + arr[i] > mid:
            cnt += 1
            pt = 0
        pt += arr[i]
    
    cnt += 1 if pt else 0

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)