import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for ai in A:
    answer += 1
    if ai - B <= 0: continue
    div, mod = divmod(ai-B, C)
    answer += div
    if mod > 0: answer += 1

print(answer)