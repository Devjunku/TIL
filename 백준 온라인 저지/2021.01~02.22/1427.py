import sys
N = list(map(int,sys.stdin.readline().rstrip()))
N = sorted(N, reverse= True)
strr = ''
for n in N:
    strr += str(n)
print(strr)