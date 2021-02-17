N1 = int(input())
n1 = N1
ans_arr = []
i = 1
num_arr = []
while i <= int(N1*(0.6) + 1):
    n1 = N1
    n2 = N1 - i + 1
    n3 = 0
    i += 1
    arr = [n1, n2]
    while True:
        n3 = n1 - n2
        if n3 < 0:
            break
        arr.append(n3)
        n1 = n2
        n2 = n3
    num_arr.append(len(arr))
    ans_arr.append(arr)
max_num = max(num_arr)
idx = num_arr.index(max_num)
print(max(num_arr))
print(*ans_arr[idx])
