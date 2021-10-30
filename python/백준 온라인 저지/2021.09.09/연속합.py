import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
maxValue = -sys.maxsize
currentValue = [0 for _  in range(n)]

for i in range(n):
    currentValue[i] = max(currentValue[i-1]+nums[i], nums[i])
    maxValue = max(maxValue, currentValue[i])

print(maxValue)