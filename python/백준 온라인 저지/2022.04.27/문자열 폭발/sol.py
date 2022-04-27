import sys
input = sys.stdin.readline

stack = []

sang_string, bomb_string = input().strip(), input().strip()
bomb_num = len(bomb_string)
for s in sang_string:
    if len(stack) < bomb_num:
        stack.append(s)
    else:
        confirm_string = ""
        for i in range(-bomb_num, 0):
            confirm_string += stack[i]
        if confirm_string == bomb_string:
            for _ in range(bomb_num):
                stack.pop()
        stack.append(s)

if len(stack) >= bomb_num:
    confirm_string = ""
    for i in range(-bomb_num, 0):
        confirm_string += stack[i]
    if confirm_string == bomb_string:
        for _ in range(bomb_num):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")