# 커피자판기_2
# while_4.py

coffee = 10
while True: # 무한루프 => 반드시 break문이 있어야 탈출함.
    money = int(input("돈을 넣어주세요: "))  #그냥 input만 쓰면 입력값을 문자로 저장함
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1 # coffee = coffee -1 과 같다.
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    print("남은 커피의 양은 %d개입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
