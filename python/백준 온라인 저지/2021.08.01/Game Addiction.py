H, N = map(int, input().split())
d = abs(H-N)

res1 = 1
res2 = 1
for i in range(2, 2*d+1):
    res1 *= i

for i in range(2, d+1):
    res2 *= i

res = (res1)//(res2**2)

print(res)