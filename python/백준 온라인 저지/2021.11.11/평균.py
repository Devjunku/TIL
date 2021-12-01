from statistics import mean
N = int(input())
scores = list(map(float, input().split()))

M = max(scores)
for i in range(N):
        scores[i] = scores[i]/M * 100
print(mean(scores))