import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0

for i in range(n):
    sub = arr[:i] + arr[i+1:]
    start, end = 0, len(sub) - 1

    while start < end:
        mid = sub[start] + sub[end]

        if arr[i] == mid:
            answer += 1
            break
        elif arr[i] > mid:
            start += 1
        else:
            end -= 1
    
print(answer)



