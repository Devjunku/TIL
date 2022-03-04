import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

alpha_key = {
    "a": True,
    "b": False,
    "c": True,
    "d": False,
    "e": False,
    "f": False,
    "g": False,
    "h": False,
    "i": True,
    "j": False,
    "k": False,
    "l": False,
    "n": True,
    "m": False,
    "o": False, 
    "p": False,
    "q": False,
    "r": False,
    "s": False,
    "t": True,
    "u": False,
    "v": False,
    "w": False,
    "x": False,
    "y": False,
    "z": False
    }
another_alpha_key = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_value = [0] * len(alpha_key)
# 배우는 단어의 개수가 4개 이하면 아에 아무 단어도 못읽음

u = k - 5
if u < 0:
    print(0)
else:
    com_learning_alpha = combinations(another_alpha_key, u)

    answer = 0
    for com in com_learning_alpha:
        for c in com:
            alpha_key[c] = True
        
        cnt = 0
        toggle = False
        for word in words:
            for s in word:
                if not alpha_key[s]:
                    toggle = True
                    break
            
            if toggle:
                toggle = False
                continue
            else: cnt += 1
        
        answer = max(cnt, answer)
        for c in com:
            alpha_key[c] = False

    print(answer)