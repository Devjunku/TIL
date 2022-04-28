import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

differ = 2000000001
answer = [arr[0], arr[n-1]]
while left < right:
    value = arr[left] + arr[right]
    if abs(differ) >= abs(value):
        differ = value
        answer[0] = arr[left]
        answer[1] = arr[right]
    if value < 0:
        left += 1
    elif value > 0:
        right -= 1
    else:
        break
print(f"{answer[0]} {answer[1]}")