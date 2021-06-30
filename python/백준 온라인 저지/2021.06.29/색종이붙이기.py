N = int(input())

paper = [[0]*1001 for _ in range(1001)]

x1 = []
y1 = []
x2 = []
y2 = []

for _ in range(N):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x1.append(x_1)
    y1.append(y_1)
    x2.append(x_1 + x_2)
    y2.append(y_1 + y_2)

answer = []
for s1, e1, s2, e2 in zip(x1[::-1], x2[::-1], y1[::-1], y2[::-1]):
    seen = 0
    for i in range(s1, e1):
        for j in range(s2, e2):
            if not paper[i][j]:
                seen += 1
                paper[i][j] = 1

    answer.append(seen)

for a in answer[::-1]:
    print(a)
