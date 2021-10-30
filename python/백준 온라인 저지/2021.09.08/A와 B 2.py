import sys
input = sys.stdin.readline

s = input().strip()
t = list(input().strip())

def dfs(string):
    if len(string) <= len(s):
        if "".join(string) == s:
            print(1)
            exit(0)
        return
    
    if string[0] == 'B':
        string = string[::-1]
        string.pop()
        dfs(string)
        string.append('B')
        string = string[::-1]

    if string[-1] =='A':
        string.pop()
        dfs(string)
        string.append('A')
    
dfs(t)
if not dfs(t):
    print(0)
