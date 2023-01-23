import sys
input = sys.stdin.readline

# N -> 1 <= N <= 9

N = int(input())

for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")