import sys

input = sys.stdin.readline

while 1:
    string = input().rstrip()
    stack = []
    true_flag = 1
    for cha in string:
        if cha == '(' or cha =='[':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = 0
                break
        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break
    if string == '.':
        break
    print('yes' if true_flag and not (stack) else 'no')



##### 선규님 코드 #####


while True:
    s = input()
    if s == '.':
        break
    cnt = 0
    result = ''
    li = [-1]
    for i in s:
        if i in ['(', '[']:
           li.append(i)
           cnt += 1
        elif i in [')', ']']:
            if li[-1] == '(' and i == ')':
                li.pop()
                cnt -= 1
            elif li[-1] == '[' and i == ']':
                li.pop()
                cnt -= 1
            else:
                cnt += 1
                break
    if not cnt:
        result = 'yes'
    else:
        result = 'no'
    print(result)