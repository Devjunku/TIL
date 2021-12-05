l, c = map(int, input().split())
string = list(map(str, input().split()))
ans_ele = []
answer = []

string.sort()

def away_string(num, idx, l_n, c_n):
    if num == l:
        answer.append("".join(ans_ele))
        return

    for i in range(idx, c_n):
        ans_ele.append(string[i])
        away_string(num+1, i+1, l_n, c_n)
        ans_ele.pop()

def confirm(argument):
    for i in argument:
        v_idx = 0
        c_idx = 0
        for j in i:
            if j in 'aeiou':
                c_idx += 1
            else:
                v_idx += 1
        if c_idx >= 1 and v_idx >= 2:
            print(i)
    return

away_string(0, 0, l, c)
confirm(answer)