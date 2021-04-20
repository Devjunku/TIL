from sys import stdin

N = int(stdin.readline().rstrip())

arr = []
for _ in range(N):
    arr.append(list(map(int, stdin.readline().rstrip().split())))
ban = [[0, 5], [1, 3], [2, 4]]
max_num = []
for i in range(3):
    total = 0
    for j in range(len(arr)):
        arr[j]


        total += max(arr[j])
    max_num.append(total)
print(max(max_num))

    
