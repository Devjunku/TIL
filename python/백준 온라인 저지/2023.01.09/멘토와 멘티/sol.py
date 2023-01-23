import sys
input = sys.stdin.readline

n = int(input())

data = []

for _ in range(n):
    mento, mentee = input().strip().split()
    data.append((mento, mentee))
    
data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[0], reverse=True)

for i in range(n-1, -1, -1):
    print(data[i])