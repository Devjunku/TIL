
s = input()
for ss in range(len(s)):
    if  s[ss:]==s[ss:][::-1]:
        print(len(s)+i)
        break
    

s=input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break