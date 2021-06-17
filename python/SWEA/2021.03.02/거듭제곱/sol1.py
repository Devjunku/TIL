import sys

sys.stdin = open('input.txt')

def recursive(n):
    if n == 1:
        return a
    return a * recursive(n-1)


for _ in range(1, 11):
    t = int(input())
    a, b = map(int, input().split())
    print('#{} {}'.format(t, recursive(b)))
