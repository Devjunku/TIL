def solution(record):

    roc = []
    dic = {}
    for r in record:
        rs = r.split(" ")
        if rs[0] != "Leave":
            dic[rs[1]] = rs[2]
        roc.append((rs[0], rs[1]))

    answer = []
    for r in roc:
        behave, i_d = r
        if behave == "Enter":
            answer.append(f"{dic[i_d]}님이 들어왔습니다.")
        elif behave == "Leave":
            answer.append(f"{dic[i_d]}님이 나갔습니다.")
    
    return answer


if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))