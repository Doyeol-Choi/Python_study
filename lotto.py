# 로또번호 자동 생성(단 한번)

# import random

# lotto = []
# while True:
#     a = random.randint(1,45)    # 1~45까지의 정수를 랜덤 발생
#     if a in lotto:  # in 속하는 / not in 속하지 않은
#         print(f"{a} 중복되었습니다.")
#     else:
#         lotto.append(a)
#         if len(lotto) == 6:
#             break
        
# print(lotto)


# 로또번호 자동생성 무한반복

import random

def lotto_gen():
    lotto = []
    while True:
        num = random.randint(1,45)
        if num in lotto:
            print(f'{num} 중복되었습니다.')
        else:
            lotto.append(num)
            if len(lotto) == 6:
                break
            
    print(lotto)

    
while 1:
    ans = input("로또번호 자동생성기입니다. 계속하시겠습니까> (y/n) : ")
    if ans in ("Y", "y"):   
    # if (ans == "y") or (ans == "Y"):
        lotto_gen()
        
    else:
        print("종료합니다.")
        break