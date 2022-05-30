# 학점 출력

# score = int(input("점수를 입력해주세요>> "))

# if score >= 90:
#     print("학점은 A입니다.")
# elif score >= 80:
#     print("학점은 B입니다.")
# elif score >= 70:
#     print("학점은 C입니다.")
# elif score >= 60:
#     print("학점은 D입니다.")
# else:
#     print("학점은 F입니다.")
    
    
# 로또 번호 생성기

import random

def lotto_gen():
    lotto = []
    while True:
        num = random.randint(1,45)
        if num in lotto:
            print("중복되었습니다.")
        else:
            lotto.append(num)
            if len(lotto) == 6:
                break
    print(lotto)
        
while True:
    ans = input("로또번호 생성기 입니다. 생성하시겠습니까?(y/n)>> ")
    if ans == "y" or ans == "Y":
        lotto_gen()
    elif ans == "n" or ans == "N":
        print("종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")