from collections import deque
import sys
input = sys.stdin.readline
testcase_num = int(input())

for test in range(testcase_num):
    card_num = int(input())
    deq = deque([])
    card = deque(list(map(str, input().split())))
    while card:
        string = card.popleft()
        if not deq:
            deq.append(string)
        else:
            if ord(deq[0]) < ord(string):
                deq.append(string)
            else:
                deq.appendleft(string)
    print("".join(deq)) 