# # for문을 이용한 구구단 출력하기

# for i in range(2,10):  # 몇 단(2단~9단)
#     for j in range(1,10):   # 곱해질 수(1~9)
#         print(i * j, end=" ")   # end 이어붙이기
#     print(' ')
    
# # 이중 반복문 for
# # 먼저 안쪽 내부반복문을 모두 수행하고, 바깥쪽 외부 반복문을 수행한다.


# a = [1, 2, 3, 4]

# result = []
# for num in a:
#     result.append(num*3)
    
# print(result)


# 구구단 다른방법

# result = [x*y for x in range(2,10) for y in range(1,10)]

# print(result)

# 1부터 1000까지의 수중에서 3의 배수의 합을 구해보자
# result : 결과 출력변수
# while 문 사용

# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#         print(i, end=" ")
#     i += 1
# print("")            
# print(result)

# for문으로

# result=0
# for i in range(1,1001):
#     if i % 3 == 0:
#         result += i
        
# print(result)


# 3의 배수이면서 5의 배수인 수를 출력하고, 마지막에 누적값을 출력하라

# result = 0
# i = 1
# while i <= 100:
#     if (i % 3 == 0) and (i % 5 == 0):
#         result += i
#         print(i, end=" ")
#     i += 1
# print("")
# print(result)


# *
# **
# ***
# ****
# *****     출력하기

i = 0
while True:
    i += 1
    if i > 5: break
    print('*'*i)


# 위의 것 반대로 출력하기

# i = 5
while True:
    if i <= 0: break
    print('*'*i)
    i -= 1