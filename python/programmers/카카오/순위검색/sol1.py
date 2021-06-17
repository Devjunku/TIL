# 효율성 탈락
def solution(info, query):
    
    answer = []
    for q in query:
        e_query = q.split(' and ')
        e_query = e_query[:-1] + e_query[-1].split()
        num = 0
        for i in range(len(info)):
            e_info = info[i].split()
            cnt = 0
            for j in range(5):
                if j != 4:
                    if e_query[j] == '-':
                        cnt += 1
                    elif e_query[j] == e_info[j]:
                        cnt += 1
                else:
                    if int(e_query[j]) <= int(e_info[j]):
                        cnt += 1
                    
            if cnt == 5:
                num += 1

        answer.append(num)

    return answer


if __name__ == '__main__':
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))