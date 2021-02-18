n, m = map(int, input().split())

length = list(map(int, input().split()))

start = 0
end = max(length)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(len(length)):
        if length[i] > mid:
            total += length[i] - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
