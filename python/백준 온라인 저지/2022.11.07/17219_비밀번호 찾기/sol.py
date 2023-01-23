import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}

for _ in range(N):
    email, pwd = input().strip().split()
    dic[email] = pwd

for _ in range(M):
    email = input().strip()
    print(dic[email])