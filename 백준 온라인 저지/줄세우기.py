N = int(input())

number = list(map(int, input().split()))
idx = list(range(2, N+1))

arr = [1]
for s, i in zip(number[1::], idx):
    arr.insert(s,i)
print(*arr[::-1])