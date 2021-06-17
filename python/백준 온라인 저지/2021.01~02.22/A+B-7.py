import sys

T = int(sys.stdin.readline().rstrip())

for t in range(1, T+1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{t}: {A+B}')