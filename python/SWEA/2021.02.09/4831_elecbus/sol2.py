T = int(input())

for tc in range(1, T+1):
    # K : 이동할 수 있는 거리
    # N : 마지막 종점의 위치
    # M : 충전소의 개수
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)

    # for i in range(M):
    #     bus_stop[charge[i]] = 1

    for i in charge:
        bus_stop[i] = 1

    bus = 0 #버스 위치
    ans = 0 #충전 횟수

    while True:
        bus += K
        if bus >= N: break # 종점에 도착하거나 종점을 지나 더 나아간 경우

        for i in range(bus, bus-K, -1):
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus = i
                break
        else: # 충전기를 못찾았을 때
            ans = 0
            break
    print('#{} {}'.format(tc, ans))



################################################
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    ans = 0

    charge = [0] + charge + [N]

    last = 0

    # 충전소에 출발점과 도찰지를 넣어놓았으므로
    for i in range(1, M+2):
        if charge[i] - charge[i-1] > K:
            ans = 0
            break
        #갈 수 있으면, 아무작업 x
        #갈 수 없다면, 내 바로 직전 충전소로 위치를 옮기고 횟수 1회증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1
    print('#{} {}'.format(t, ans))






