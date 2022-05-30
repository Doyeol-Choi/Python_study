# 나무 찍기
# while_1.py

treeHit = 0 # 나무 찍은 횟수
while treeHit < 10: # 나무를 찍은 횟수가 10보다 작은 동안 반복하라
                    # treeHit < 10 조건에 만족할때만 아래로 내려감.
                    # 그렇지 않으면(거짓) while문을 탈출한다.
    treeHit = treeHit + 1   # treeHit += 1, treeHit++은 C 나 java에서 사용가능
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")
        
# 캡처 단축키 : 윈도우키 + Shift + S