# 버블 정렬

def BobbleSort(ex_list):
    for i in range(len(ex_list)-1, 0, -1): # 범위 끝 위치를 지정
        for j in range(0, i): 
            if ex_list[j] > ex_list[j+1]: # 인접한 값을 비교후 조건이 만족되면
                ex_list[j], ex_list[j+1] = ex_list[j+1], ex_list[j] # 그 둘을 뒤바꿈, 바꿀 때, 이 연산은 파이썬에서 튜플로 작동

# 버블 정렬의 경우 시간 복잡도가 O(N**2)으로 작동
# 많이 이용하는 정렬임
# 하지만, 시간 복잡도가 큰 탓에 다량의 데이터에서
# 좋은 성능을 보이지 못함