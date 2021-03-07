def post_expression(string):
    stack = []
    str_list = list(string)
    res = ''
    for s in str_list:
        if s != '*' and s != '/' and s != '+' and s != '-' and s != '(' and s != ')':
            res += s
        else:
            if s == '(':
                stack.append(s)
            elif s == '*' or s == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(s)
            elif s == '+' or s == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(s)
            elif s == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    
    while stack:
        res += stack.pop()
    
    return res

string = input()
print(post_expression(string))