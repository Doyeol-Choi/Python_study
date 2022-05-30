# 색상테마변경 Ctrl + K + T
# 지역변수, 전역변수 비교

gun = 10

def checkpoint(soldiers):
    global gun  # 전역변수로 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    
print("전체 총 : {0}".format(gun))

checkpoint(2)   # 경계근무를 2명 보냄
print("남은 총 : {0}".format(gun))

# 일반적으로실무에서는 global 전역변수를 사용하지 않는다.
# 전역변수를 많이 사용하게 되면 코드 해석이 어려워짐.
# 로컬변수를 사용하되 return으로 돌려 준다.


print()

gun = 10

def checkpoint_ret(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))

# 2명의 병사가 경계근무를 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))