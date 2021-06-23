from itertools import combinations


def solution(relation):
    
    ans = 0
    all = []
    u = []

    row = len(relation)

    if row:
        
        col = len(relation[0])

        # 나올 수 있는 조합 구성
        for i in range(1, col+1):
            all.extend([set(k) for k in combinations([j for j in range(col)], i)])
        # print(all)

        # 유일성 검증
        for ae in all:
            u_e = set()
            for r in range(row):
                temp = ''
                for e in ae:
                    temp += str(relation[r][e])
                u_e.add(temp)

            if len(u_e) == row:
                u.append(ae)
        # 최소성 검증
        d_u = set()
        for i in u:
            for j in u:
                if i.issubset(j) and i != j:
                    d_u.add(u.index(j))

        ans = len(u) - len(d_u)

        return ans
        
    else:
        return ans
        




if __name__ == "__main__":
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))