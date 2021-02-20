from sys import stdin

N = int(stdin.readline().rstrip())

cnt = 0
for n in range(N):
    string = stdin.readline().rstrip()
    arr = [] # 빈 리스트 할당
    cnt += 1 # 일단 단어가 있으면 하나를 세고
    for s in range(len(string)): # 문자 개수 만큼 순회
        if string[s] not in arr: # 만약에 문자가 arr에 없으면
            arr.append(string[s]) # 추가 시킴
            continue # 그리고 나머지는 무시
        elif string[s-1] == string[s]: #그렇지 않으면 이미 존재하는 문자
            continue # 대신에 전과 같으면 괜찮으므로 다시 무시
        else: # 위 2개의 조건에 해당하지 않으면, 문제의 조건에 안맞는 것이므로
            cnt -= 1 # cnt에서 1을 빼버림(해당 단어를 세지 않음)
            break # 더 이상 순회할 의미가 없으므로 순회 정지
print(cnt) # cnt 출력