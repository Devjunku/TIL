from collections import deque

def is_x(string):
    string = list(string)
    for i in range(len(string)-2):
        if ''.join(string[i:i+3]) == '110':
            string.pop(i)
            string.pop(i)
            string.pop(i)
    
    return string
        


def solution(s):

    ans = []
    for ss in s:
        
        ele = []
        e_string = is_x(ss)
        q = deque([ss])

        while q:
            sss = q.popleft()
            e_string = is_x(sss)
            for i in range(len(sss)):
                a = ''.join(e_string[:i]) + '110' + ''.join(e_string[i:])
                if a in ele:
                    continue
                else:
                    ele.append(a)
                    q.append(a.split())
        
        ans.append(sorted(ele)[0])

    return ans


if '__main__' == __name__:
    print(solution(["1110","100111100","0111111010"]))
    