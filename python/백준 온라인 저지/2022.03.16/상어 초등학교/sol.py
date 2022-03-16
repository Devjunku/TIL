import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n**2):
    idx, s1, s2, s3, s4 = map(int, input().split())
    dic[idx] = (s1, s2, s3, s4)

visited = [False for _ in range(n**2)]

room = [[-1]]

