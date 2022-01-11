import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

n_dic = {}
answer = []

for _ in range(n):
    string = input().strip()
    n_dic[string] = 1

for _ in range(m):
    string = input().strip()
    try:
        n_dic[string]
        answer.append(string)
    except:
        continue

answer.sort()
l = len(answer)
print(l)
for i in range(l):
    print(answer[i])