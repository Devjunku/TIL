n = int(input())
info = []
for _ in range(n):
    info.append(input().split())
# print(info)
stack = []

for i_f in info:
    if i_f[0] == 'push':
        stack.append(i_f[1])
    elif i_f[0] == 'top':
        if len(stack) == 0:
            print(-1)
            continue
        else:
            print(stack[-1])
            continue
    elif i_f[0] == 'size':
        print(len(stack))
        continue
    elif i_f[0] == 'empty':
        if len(stack) == 0:
            print(1)
            continue
        else:
            print(0)
            continue
    elif i_f[0] == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        else:
            print(stack.pop())

    