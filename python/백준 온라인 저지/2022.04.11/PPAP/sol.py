import sys
input = sys.stdin.readline

stack = []

ppap = list(input().strip())

for p in ppap:
    stack.append(p)
    if len(stack) >= 4:
        if stack[-4] + stack[-3] + stack[-2] + stack[-1] == "PPAP":
            for _ in range(4):
                stack.pop()
            stack.append("P")

if stack == ["P"]:
    print("PPAP")
else:
    print("NP")