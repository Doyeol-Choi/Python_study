# 정보처리기사 실기 기출문제1(5점)
"""
asia = {'한국', '중국', '일본'} # 집합(set)
asia.add('베트남')  # add_한개의 값 추가
asia.add('중국')    # 중복값은 한번만 추가됨
asia.remove('일본') # remove 해당값 제거됨
asia.update({'한국', '홍콩', '태국'})   # update 여러개 값 추가시
print(asia)
"""
# 답 {'한국', '중국', '베트남', '홍콩', '태국'} 집합의 순서는 무관하다.



# 정보처리기사 실기 기출문제2(5점)

lol = [[1,2,3],[4,5],[6,7,8,9]]
print(lol[0])       # [1,2,3]
print(lol[2][1])    # 7
for sub in lol:                 # sub는 lol[0], lol[1], lol[2] 를 순서대로 가져온다
    for item in sub:            # 
        print(item, end=' ')    # item을 출력하고 end는 줄을 바꾸지말고 end출력후 계속 작성
    print()                     # 줄바꿈의 의미
    
# 실행결과
# [1, 2, 3]
# 7
# 1 2 3
# 4 5
# 6 7 8 9