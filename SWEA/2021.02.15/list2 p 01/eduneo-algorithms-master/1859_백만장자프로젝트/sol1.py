import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    length = int(input())
    l = list(map(int, input().split()))
    print(length, len(l))

