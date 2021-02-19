import sys

sys.stdin = open('sample_input.txt')



T = int(input())

for t in range(1,T+1):

    arr = [list(input()) for _ in range(5)]

    max_col = len(arr[0])
    for i in range(1, len(arr)):
        if len(arr[i]) > max_col:
            max_col = len(arr[i])


    ans = ''
    for i in range(max_col):
        for j in range(len(arr)):
            if i < len(arr[j]):
                ans += arr[j][i]
            # try:
            #     print(arr[j][i], end ="")
            # except:
            #     pass
    print('#{} {}'.format(t,ans))