from collections import deque
import sys
input = sys.stdin.readline

wheels = [
    [],
    deque([]),
    deque([]),
    deque([]),
    deque([])
]

for i in range(1, 5):
    data = list(input().strip())
    for d in data:
        wheels[i].append("N" if d == "0" else "S")

k = int(input())

# TODO
# 2, 5 index가 S과 N극이면 돌아감
# 그렇지 않으면 안돌아감

def circling_wheel(start, order):

    wheels[start].rotate(order)

    if len(adj_num[start]) == 0: return

    visited[start] = True

    for nxt in adj_num[start]:
        if not visited[nxt]:
            circling_wheel(nxt, order*-1)

for _ in range(k):
    num, order = map(int, input().split())

    adj_num = [[] for _ in range(5)]
    visited = [0] * 5

    if wheels[1][2] != wheels[2][6]: 
        adj_num[1].append(2)
        adj_num[2].append(1)
    if wheels[2][2] != wheels[3][6]:
        adj_num[2].append(3)
        adj_num[3].append(2)
    if wheels[3][2] != wheels[4][6]:
        adj_num[3].append(4)
        adj_num[4].append(3)

    circling_wheel(num, order)

answer = 0
if wheels[1][0] == "S": answer += 1
if wheels[2][0] == "S": answer += 2
if wheels[3][0] == "S": answer += 4
if wheels[4][0] == "S": answer += 8
print(answer)