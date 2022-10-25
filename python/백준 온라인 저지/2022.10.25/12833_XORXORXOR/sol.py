import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
answer1 = a ^ b
answer2 = answer1 ^ b
print(answer1) if c % 2 == 1 else print(answer2)