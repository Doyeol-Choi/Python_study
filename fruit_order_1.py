import datetime
now = datetime.datetime.now()
import random
jaum = 'bcdfghhklmnpqrstvwxz'
moum = 'aeiouy'
sn = ""
for j in range(4):
    if j%2 == 0:
        sn += random.choice(jaum)   # choice는 예약어 jaum에서 랜덤하게 하나 가져온다
    else:
        sn += random.choice(moum)

def order_get(order):
    if order == fruit2[0]:
        order2 = fruit_list[0]
        price = price_list[0]
        print("{0} 상품을 선택하셨습니다. 가격은 {1:,}원입니다.".format(order, fruit.get(order2)))
    elif order == fruit2[1]:
        order2 = fruit_list[1]
        price = price_list[1]
        print("{0} 상품을 선택하셨습니다. 가격은 {1:,}원입니다.".format(order, fruit.get(order2)))
    elif order == fruit2[2]:
        order2 = fruit_list[2]
        price = price_list[2]
        print("{0} 상품을 선택하셨습니다. 가격은 {1:,}원입니다.".format(order, fruit.get(order2)))
    elif order == fruit2[3]:
        order2 = fruit_list[3]
        price = price_list[3]
        print("{0} 상품을 선택하셨습니다. 가격은 {1:,}원입니다.".format(order, fruit.get(order2)))
    return price
'''
문제의 시작 상품주문 리스트는 그냥
information = """
[상품리스트]
사과(5kg)       19,900원 딸기(500g)  13,500원
바나나(1.5kg)    6,900원 포도(1.8kg) 14,800원   
"""
으로 넣고 딕셔너리에 kg들은 빼면 훨씬 간단해진다...
'''
fruit = {'사과(5kg)': 19900, '딸기(500g)': 13500, '바나나(1.5kg)': 6900, '포도(1.8kg)': 14800}
fruit_list = list(fruit.keys())
price_list = list(fruit.values())
print("[상품주문리스트]")
print("{0:<12}{1:>6,}원".format(fruit_list[0],price_list[0]), end =" ")
print("{0:<12}{1:>6,}원".format(fruit_list[1],price_list[1]))
print("{0:<12}{1:>6,}원".format(fruit_list[2],price_list[2]), end =" ")
print("{0:<12}{1:>6,}원".format(fruit_list[3],price_list[3]))
fruit2 = [fruit_list[0].split("(")[0],fruit_list[1].split("(")[0],fruit_list[2].split("(")[0],fruit_list[3].split("(")[0]]
print("\n[현재 주문 가능한 상품]")
print(f"{fruit2[0]}\n{fruit2[1]}\n{fruit2[2]}\n{fruit2[3]}")

toggle = True

while toggle:    
    ans = input("\n상품을 주문하시겠습니까? (Y/N) : ")
    if ans in ['y','Y']:
        order = input("주문할 상품명을 입력하세요 : ")
        if order in fruit2:
            price = order_get(order)
            while toggle:
                many = int(input("주문하실 수량을 입력해주세요 : "))
                if many > 30:
                    print("재고가 부족합니다 수량을 다시 입력해주세요")
                elif 0 < many <= 30:
                    print(f"주문하실 상품의 수량은 {many} 박스(팩)입니다.\n")
                    print('======주문내역======')
                    print("상품명".ljust(5),"수량".rjust(7))
                    print("{:<5}{:>10}".format(order, many))
                    print('-'*20)
                    print("결재가격 : {:,}원".format(price*many))
                    print('='*20)
                    while toggle:
                        end = input("주문을 완료하시겠습니까? (Y/N) : ")
                        if end in ['y','Y']:
                            print("주문이 완료되었습니다.")
                            print("주문 시각은 {}월 {}일 {}시 {}분 입니다.".format(now.month, now.day, now.hour, now.minute))
                            print("주문번호는 {0}{1:0>2}{2}{3} 입니다.".format(now.year,now.month,now.day,sn))
                            toggle = False
                        elif end in ['n','N']:
                            print("주문이 취소되었습니다.")
                            toggle = False
                        else:
                            print("잘못된 입력입니다. 다시 입력해주세요.")
                else:
                    print("잘못된 입력입니다. 다시 입력해주세요.")
        else:
            print("존재하지 않거나 주문이 불가능한 상품입니다.")
    elif ans in ['n','N']:
        print("주문을 종료합니다.")
        toggle = False
    else:
        print("잘못된 입력 입니다.")
