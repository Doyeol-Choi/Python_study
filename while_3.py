# 커피자판기 프로그램_while_break
# while_3.py

coffee = 10 # 자판기에 커피가 10개 재고가 있음
money = 300
while money:    # money는 0이 아닌 숫자이므로 조건의 참으로 인식됨.
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break