import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def my_MinMaxdiffer(x):
    dat1 = x[0]
    dat2 = x[0]
    for i in range(1, len(x)):
        if x[i] < dat1:
            dat1 = x[i]
        if x[i] > dat2:
            dat2 = x[i]
    return dat2 - dat1

for t in range(1,T+1):
    leng = int(input())
    data = list(map(int, input().split()))

    print('#{} {}'.format(t, my_MinMaxdiffer(data)))

