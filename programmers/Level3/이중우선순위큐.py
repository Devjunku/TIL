def solution(operations):
    
    ans = []
    
    for operation in operations:
        string, number = operation.split()
        
        if string == 'I':
            ans.append(int(number))
        else:
            if string == 'D':
                if not ans:
                    continue
                else:
                    if number == '1':
                        ans.pop()
                    elif number == '-1':
                        ans.pop(0)
        ans.sort()
        
    if ans:
        return [max(ans),min(ans)]
    else:
        return [0,0]

if __name__ == '__main__':
    print(solution(["I 16","D 1"]))
    print(solution(["I 7","I 5","I -5","D -1"]))