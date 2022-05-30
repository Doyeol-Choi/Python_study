# a=['대', '한', '민', '국']
# for i in a:
#     print(i)




# def cs(n):
#     s = 0
#     for num in range(1, n+1):
#         if num % 2 == 1:
#             s += num
#     return s
    
# print(cs(100))


# def cs(n):
#     s = 0
#     for num in range(1, n, 2):      # range(a, b, c) 는 a부터 b미만까지 c씩 증가하는 수
#         s += num
#     return s
    
# print(cs(101))



# class CharClass:
#     a = ['Seoul', 'Gyeongi', 'Inchon', 'Daejeon', 'Daegu', 'Busan']
# myVar = CharClass()
# myVar2 = CharClass()
# str01 = ''
# str02 = ''
# for i in myVar.a:
#     str01 += i[0]
# for i in myVar2.a:
#     str02 += i[-1]
# print(' '.join(str01))
# print(' '.join(str02))



# lol = [[1,2,3], [4,5], [6,7,8,9]]
# print(lol[0])
# print(lol[2][1])
# for sub in lol:
#     for item in sub:
#         print(item, end=' ')    # end 줄을 바꾸지 않고 end부분 출력 후 이어 출력
#     print()     # 개행(줄바꿈)을 위한 프린트



# asia = {'한국', '중국', '일본'}          # set(집합) 순서없고, 중복없다.
# asia.add('베트남')                      # .add 요소 하나 추가
# asia.add('중국')
# asia.remove('일본')                     # .remove 요소 하나 삭제
# asia.update({'한국', '홍콩', '태국'})   # .update set추가
# print(asia)

# sum = 0
# for i in range(1,11,2):
#     sum += i    # 1 + 3 + 5 + 7 + 9
# print(sum)

a = 100
result = 0
for i in range(1,3):
    result = a >> i
    result += 1
print(result)