import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    arr[i] += arr[i-1]

left = 0
right = 1
answer = 0
while left <= right and right < n+1:

    if arr[right] - arr[left] > m:
        left += 1
    elif arr[right] - arr[left] < m:
        right += 1
    else:
        answer += 1
        right += 1

print(answer)