# 로그인
def login(id_pw):
    while True:
        # id_pw = {'Python':'1234'}
        id = input("아이디를 입력하세요 : ")
        pw = input("비밀번호를 입력하세요 : ")
        if (id in id_pw) and (pw == id_pw.get(id)):
            print("로그인 되었습니다.")
            break
        else:
            print("잘못 입력하셨습니다.")
    return id

# 메뉴 선택
def menu():
    print('='*30)
    print('1. 입금')
    print('2. 출금')
    print('3. 잔액조회')
    print('4. 종료')
    print('5. 로그아웃')
    print('='*30)
    ans = input("원하시는 메뉴의 번호를 입력하세요 : ")
    return ans

# 입금
def deposit(id_money):
    money = int(input("입금할 금액을 입력하세요 : "))
    total = id_money.get(id) + money
    id_money.update({id:total})
    print("잔액은 {:,}원 입니다.\n".format(id_money.get(id)))

# 출금
def withdraw(id_money):
    money = int(input("출금할 금액을 입력하세요 : "))
    if money <= id_money.get(id):
        total = id_money.get(id) - money
        id_money.update({id:total})
        print("잔액은 {:,}원 입니다.\n".format(id_money.get(id)))
    else:
        print("잔액이 부족합니다. (현재잔액 : {:,}원)\n".format(id_money.get(id)))      

# 동작
id_pw = {'Python':'1234'}
id_money = {'Python':0}
end = True
while end:
    id = login(id_pw)
    while True:
        ans = menu()
        if ans == '1':
            deposit(id_money)
        elif ans == '2':
            withdraw(id_money)
        elif ans == '3':
            print("잔액은 {:,}원 입니다.\n".format(id_money.get(id)))
        elif ans == '4':
            end = False
            print("종료하겠습니다.")
            break
        elif ans == '5':
            print("로그아웃합니다.\n")
            break
        else:
            print("잘못된 입력입니다.\n")