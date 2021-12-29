import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))
end_time = arr[0][1]
answer = 1

for i in range(1, n):
    if end_time <= arr[i][0]:
        end_time = arr[i][1]
        answer += 1

print(answer)