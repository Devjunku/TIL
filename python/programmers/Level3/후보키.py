from itertools import combinations


def solution(relation):

    ans = 0
    all = []
    uniqueIndex = []

    if len(relation) > 0:
        colSize = len(relation[0])
        rowSize = len(relation)

        # 모든 조합 구하기
        for i  in range(1, colSize+1):
            all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])
        
        print(all)

        # 모든 행 분간이 가능한 경우
        for comb in all:
            vaildSet = set()
            for row in range(rowSize):
                temp = ''
                for col in comb:
                    temp += str(relation[row][col])
                vaildSet.add(temp)

                # 여기에서 유일하면 행의 갯수와 같은 것임
                # 그렇지 않다면, 행의 갯수와 같지 않을 것임

            # 행의 갯수와 같다면, 즉 유일하다면
            if len(vaildSet) == rowSize:
                # 넣어주기
                uniqueIndex.append(comb)

        print(uniqueIndex)

        #  삭제할 셋을 저장
        delSet = set()
        # 앞서 유일성이 만족된 셋을 순회
        for stdMinElem in uniqueIndex:
            for compMinElem in uniqueIndex:
                # 부분집합이면서, 같지 않으면 최소성에서 벗어남
                if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                    # 해당 인덱스만 추가
                    delSet.add(uniqueIndex.index(compMinElem))
            
        ans = len(uniqueIndex)-len(delSet)

    return ans



                

            

if __name__ == "__main__":
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))