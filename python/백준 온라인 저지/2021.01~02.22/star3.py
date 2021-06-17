N  = int(input())

star = []
for _ in range(N):
    star.append([ "*" for _ in range(N)])

# print(star)

divide = N
cnt = 0

while divide != 1:
    divide /= 3
    cnt += 1

print(divide, cnt)

for n in range(cnt):
    idx = [i for i in range(N) if (i // 3 ** n) % 3 == 1]
    print(idx)
    for i in idx:
        for j in idx:
            # print(i + 1, j + 1)
            star[i][j] = " "

for _ in star:
    print(''.join(_))

