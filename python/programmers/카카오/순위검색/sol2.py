from itertools import combinations
from bisect import bisect_left

def solution(info, query):

    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split() # 지원자 정보 분리
        my_key = infol[:-1] # 점수를 제외한 나머지 모든 정보
        myval = infol[-1] # 점수 정보

        # 키로 만들 수 있는 모든 조합을 생성
        for j in range(5): # 5개인 이유는 정보가 5개라서 그럼
            for c in combinations(my_key, j): # 조합을 돌리면 어차피 튜플형태로 나옴
                tmp = "".join(c) # 이 키들을 모두 합쳐줌
                if tmp in info_dict: # 이미 존재하면
                    info_dict[tmp].append(int(myval)) # 추가하고
                else: # 그렇지 않다면, 새로 만들되,
                    info_dict[tmp] = [int(myval)] #  리스트로 넣어줌
    
    # dictionary안의 점수 정보를 모두 정렬
    # 이걸 하는 이유가 서치를 bs로 검색하기 위해서임
    for k in info_dict:
        info_dict[k].sort()

    for qu in query: # 쿼리도 마찬가지로 보여줌
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while "and" in qu_key: # "and" 제거
            qu_key.remove("and")
        
        while "-" in qu_key: # "-" 제거
            qu_key.remove("-")
        
        qu_key = "".join(qu_key) # dict의 키처럼 문자열로 변경
        
        if qu_key in info_dict: # query의 키가 info_dict 키에 존재하면
            scores = info_dict[qu_key] # 해당 쿼리의 점수를 꺼내주고

            if scores: # scores에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
        
    return answer

if __name__ == "__main__":
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))