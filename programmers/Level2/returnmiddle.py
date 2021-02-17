def solution(s):
    if len(s) % 2 == 0:
        print(s[len(s)//2-1:len(s)//2+1]) 
    else:
        print(s[len(s)//2])

solution('abcde')