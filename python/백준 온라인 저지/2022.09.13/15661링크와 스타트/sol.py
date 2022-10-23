import sys

from numpy import full

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize

full_bit = 1
for i in range(n):
    full_bit |= 1 << i
# print(bin(full_bit)[2:])
for i in range(1, (1 << n) - 2):
    reverse = 1^full_bit
    start = 0
    link = 0
    print(bin(i)[2:], bin()[2:])

    for j in range(n):
        if (i ^ full_bit) & 1 << j: start += arr[j][]





    pass    

