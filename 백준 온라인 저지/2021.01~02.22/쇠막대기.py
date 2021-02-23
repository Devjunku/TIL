string = input().replace('()','l')
stack = 0
cnt = 0
for s in string:
    if s == '(':
        stack += 1
        cnt += 1
    elif s == 'l':
        cnt += stack
    else:
        stack -= 1
print(cnt)