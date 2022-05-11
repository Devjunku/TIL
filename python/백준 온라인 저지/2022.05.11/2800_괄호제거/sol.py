from itertools import combinations
import sys
input = sys.stdin.readline

string = input().strip()

stack = []
s_n = len(string)
loc_stack = []
for i in range(s_n):
    if string[i] == "(":
        stack.append((string[i], i))
    elif string[i] == ")":
        s, idx = stack.pop()
        loc_stack.append([idx, i])

n = len(loc_stack)

data = set()
for i in range(1, n+1):
    
    for com in list(combinations(loc_stack, i)):
        ex = []
        for c in com:
            ex.extend(c)
        
        sss = []
        for j in range(s_n):
            if j in ex: continue
            sss.append(string[j])
        
        data.add("".join(sss))

data = list(data)
data.sort()
for d in data:
    print(d)