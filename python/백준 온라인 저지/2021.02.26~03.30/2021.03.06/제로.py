K = int(input())

data = []
for _ in range(K):
    n = int(input())
    if n != 0:
        data.append(n)
    else:
        data.pop()
print(sum(data))


