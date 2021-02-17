def solution(s):
    strings = list(s)
    dat = []
    for string in strings:
        dat.append(ord(string))
    data = sorted(dat, reverse=True)
    print(data)
    answer = ''
    for dat in data:
        answer += chr(dat)
        print(chr(dat))
        print(answer)
    return answer

solution('Zbcdefg')