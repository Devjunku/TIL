import sys
N = sys.stdin.readline().rstrip()
for _ in range(int(N)):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)