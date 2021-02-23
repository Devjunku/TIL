N = int(input())
res = []
for i in range(1, N+1):
    if N == i + sum(list(map(int, list(str(i))))):
        res.append(i)
if len(res):
    print(res[0])
else:
    print(0)

            