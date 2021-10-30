import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
# while bomb in string:
#     string = string.replace(bomb, "")

# if string == "":
#     print("FRULA")
# else:
#     print(string)

stack = []
for s in string:
    stack.append(s)
    if len(stack) >= len(bomb):
        tmp = "".join(stack[-len(bomb):])
        if tmp == bomb:
            cnt = 0
            while cnt < len(bomb):
                stack.pop()
                cnt += 1

if len(stack):
    print("".join(stack))
else:
    print("FRULA")