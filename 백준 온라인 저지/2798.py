from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().strip().split())

Num = list(map(int, sys.stdin.readline().strip().split()))

com_num = combinations(Num, 3)

mylist = []
for num in com_num:
    if M-sum(num) >= 0:
        mylist.append(M-sum(num))      
print(M - min(mylist))