import sys

n = int(sys.stdin.readline().rstrip())
s1 = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
s2 = list(map(int, sys.stdin.readline().rstrip().split()))

# dic = str(cardNums.count(sangNums[0]))
# for i in range(1, K):
#     n = cardNums.count(sangNums[i])
#     dic += ' ' + str(n)
# print(dic[0:len(dic)-1])

dic = {}
for n in s1:
    try:
        dic[n] += 1
    except:
        dic[n] = 1
result = []
for i in s2:
    try:
        result.append(dic[i])
    except:
        result.append(0)

for i in result:
    print(i, end = ' ')