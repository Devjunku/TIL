import sys
input = sys.stdin.readline

stack = []

ppap = list(input().strip())

for s in ppap:
    stack.append(s)
    if len(stack) >= 4:
        if stack[-4] + stack[-3] + stack[-2] + stack[-1] == "PPAP":
            for _ in range(4):
                stack.pop()
            stack.append("P")

if "A" in stack:
    print("NP")
else:
    if len(stack) > 1:
        print("NP")
    else:
        print("PPAP")