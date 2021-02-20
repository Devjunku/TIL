from sys import stdin

string = stdin.readline().rstrip()

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

i = 0
j = 0
cnt = 0
while True:
    j += 1
    if string[i:i+j] in alphabet:
        # print(string[i:i+j])
        cnt += 1
        i += j
        j = 0
    elif j > 2 and string[i:i+j] not in alphabet:
        # print(string[i:i+j])
        cnt += 1
        i += 1
        j = 0

    if j > 2:
        j = 0

    if i >= len(string):
        break

print(cnt)

     
