def solution(name):
    cnt = 0
    for na in name:
        # print(ord(na) - ord('A'))
        # print(1 + (ord('Z') - ord(na)))
        if (ord(na) - ord('A')) <= (1 + (ord('Z') - ord(na))):
            cnt += (ord(na) - ord('A'))
        else:
            cnt += (1 + (ord('Z') - ord(na)))
        

    cnt += len(name) - 1
    return cnt

# print(ord('A'))

if __name__ == "__main__":
    print(solution('JEROEN'))
    print(solution('JAN'))