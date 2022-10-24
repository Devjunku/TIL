import sys
input = sys.stdin.readline

n, k = int(input()), int(input())

card_list = [input().strip() for _ in range(n)]
answer = set()

def recursive(idx, number, idxs):

    if idx == k:
        answer.add("".join(number))
        return
    
    for i in range(n):
        if i in idxs: continue
        idxs.append(i)
        number.append(card_list[i])
        recursive(idx + 1, number, idxs)
        number.pop()
        idxs.pop()

recursive(0, [], [])
print(len(answer))