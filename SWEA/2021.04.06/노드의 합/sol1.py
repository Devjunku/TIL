import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    N_list = [0] * (N+1)

    for _ in range(M):
        n1, n2 = map(int, input().split())
        N_list[n1] = n2

    # 노드의 갯수가 짝수 일수도 홀수 일수도 있음
    i = N
    if N % 2 == 0: # 짝수이면
        N_list[i//2] += N_list[i] # 맨뒤에 일단 누적(하나 밖에 없기 때문에)
        i -= 1 # 1는 여기서 1을 빼주고

    while i > L: # 이제 해당 목표 노드의 인덱스까지 꺼꾸로 연산을 시작
        N_list[i // 2] += N_list[i] # 누적
        N_list[i // 2] += N_list[i-1] # 누적
        i -= 2 # 2번 연산했으니 2번 빼주기

    print('#{} {}'.format(t, N_list[L]))










