import sys
input = sys.stdin.readline

H, M = map(int, input().split())

total_time = H * 60 + M
total_time += int(input())

if 60 * 24 <= total_time:
    total_time -= (60 * 24)
    
div, mod = divmod(total_time, 60)
print(div, mod)