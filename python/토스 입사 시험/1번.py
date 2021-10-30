def solution(name_list):
    name_dic = {}
    answer = []
    alphabet = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for name in name_list:
        if name in name_dic.keys():
            name_dic[name] += 1
            answer.append(name+alphabet[name_dic[name]])
        else:
            name_dic[name] = 0
            answer.append(name+alphabet[0])

    return answer

if __name__ == '__main__':
    print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))