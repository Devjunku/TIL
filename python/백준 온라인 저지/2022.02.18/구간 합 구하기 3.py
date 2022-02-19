import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] + list(map(int, input().split())) for _ in range(n)]

