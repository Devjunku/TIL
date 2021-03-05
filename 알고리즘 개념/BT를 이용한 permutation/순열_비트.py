arr = [1, 2, 3]
N = 3
sel = [0] * N # 뽑은 결과들이 저장될 리스트

# check는 10진수 정수
def perm(idx, check):
    if idx == N:

        return sel

    for j in range(N):
        if check & (1<<j): continue

        sel[idx] = arr[j]
        perm(idx+1, check | (1<<j)) # check 전달을 이렇게 해야함 근데 여기서는
                                    # 원상복귀 과정이 필요없음 저거 일회성임

print(perm(0, 0))


