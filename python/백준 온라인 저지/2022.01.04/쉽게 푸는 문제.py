A, B = map(int, input().split())

answer = [0]

for i in range(1, 46):
    for j in range(i):
        answer.append(i)

for i in range(1, len(answer)):
    answer[i] += answer[i-1]

print(answer[B] - answer[A-1])