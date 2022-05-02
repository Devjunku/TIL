import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

dic = {}
for ai in set(arr):
    dic[ai] = 0

left = 0
right = 0

answer = 0

while left <= right and right < n:
    answer = max(answer, right - left)
    print(right, left)
    dic[arr[right]] += 1
    if dic[arr[right]] > k:
        dic[arr[left]] -= 1
        left += 1
    elif dic[arr[right]] <= k:
        right += 1

print(answer)