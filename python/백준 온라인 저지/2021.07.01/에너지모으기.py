import sys
N = int(input())
w_i = list(map(int, input().split()))

max_ = -sys.maxsize

def tracking(n, w_i, sum_):
    global max_

    # 남은 개수가 2개 이하인 경우 바로 리턴
    if n <= 2:
        if sum_ > max_:
            max_ = sum_
        return

    for i in range(1, n-1):
        cont = (w_i[i-1] * w_i[i+1])
        save = w_i.pop(i)
        tracking(n-1, w_i, sum_ + cont)
        w_i.insert(i, save)
    
tracking(N, w_i, 0)
print(max_)