# 동적 언어라고 했지만
# 정적 데이터 타입이 있다. Tuple -> 데이터 변환이 불가능

# mutable

a = 1
b = a

print(1 == "1")


# Immutable

# a = 1
# a = 2

# array 배열

# index -> 색인, 목차
# List
# tuple

# 가정법

# 연산자

# +, -, *, /
# 4 3 -> 1

# // -> 몫 연산자
# % -> 나머지 연산자
# 몫과 나머지를 구해주는 함수

a, b = divmod(4,2)
# print(a)
# print(b)


# if a == b: print(1)
# else: print(2)

# == -> 같은가?
# != -> 같지 않은가?

# if a is not b: print(1)
# else: print(2)

# if not (a is b): print(1)
# else: print(2)

# T 그리고 T -> T
# T 그리고 F -> F
# F 그리고 T -> F
# F 그리고 F -> F

# T 또는 T -> T
# T 또는 F -> T
# F 또는 T -> T
# F 또는 F -> F

# True, False

# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)

# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)

# a = 1
# b = 2

# if a > b: print(">")
# elif a < b: print("<")
# else: print("==")



a = 80

if 90 < a <= 100:
    print("good")
elif 80 < a <= 90:
    print("soso")
else:
    print("Not Bad")


# 반복문
# 1. for -> 프로그래머가 횟수를 정해서 정해진 횟수만 반복한다.
# 2. while -> 조건이 만족되지 않으면 탈출해
# 3. repeat -> 조건이 만족되면 탈출 -> 조건을 너가 지정해줘야함.
# 무한 루프가 돌 수 있다.

a = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in range(0, len(a)):
#     print(a[i], end=" ")

# i = 0
# while i < len(a):
#     print(a[i], end=" ")
#     i += 1

for i in range(0, 10, 3):
    print(i, end=" ")




# print(list(range(0, len(a))))
# list(range(0, 8)) -> 0, 1, 2, 3, 4, 5, 6, 7
# 0, 1, 2, 3, 4


