def solution(str1, str2):

    dic1 = {}
    dic2 = {}
    str1 = str1.upper()
    str2 = str2.upper()
    cross_set = {}

    for i in range(len(str1)-1):
        s1 = str1[i:i+2]
        if s1.isalpha():
            if s1 in dic1.keys():
                dic1[s1] += 1
            else:
                dic1[s1] = 1

    for i in range(len(str2)-1):
        s2 = str2[i:i+2]
        if s2.isalpha():
            if s2 in dic2.keys():
                dic2[s2] += 1
            else:
                dic2[s2] = 1

    full_set = dic1

    for key, value in dic2.items():
        # 교집합
        if key in dic1.keys():
            if value > dic1[key]:
                cross_set[key] = dic1[key]
                full_set[key] = value
            else:
                cross_set[key] = value
                full_set[key] = dic1[key]
        else:
            full_set[key] = value

    c_v = 0
    f_v = 0

    for v in cross_set.values():
        c_v += v
    
    for v in full_set.values():
        f_v += v

    if c_v == 0 and f_v == 0:
        return 65536
    else:
        return int(65536*(c_v/f_v))


if __name__ == '__main__':
    print(solution('FRANCE', 'french'))
    print(solution('handshake', 'shake hands'))
    print(solution('aa1+aa2', 'AAAA12'))
    print(solution('E=M*C^2', 'e=m*c^2'))