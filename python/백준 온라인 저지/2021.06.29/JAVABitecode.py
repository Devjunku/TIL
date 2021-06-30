import sys
input = sys.stdin.readline

N = int(input())
string = list(input())

ans = []
for s in string:
    if s not in ['A','J','V']: ans.append(s)

print(''.join(ans)) if ans else print('nojava')