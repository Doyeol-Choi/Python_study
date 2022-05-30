import datetime
import random

endcd = True
jaum = 'bcdfghhklmnpqrstvwxz'
moum = 'aeiouy'
sn = ""

for j in range(4):
    if j%2 == 0:
        sn += random.choice(jaum)
    else:
        sn += random.choice(moum)
# print(sn)

def Odr():
    while True:
        Sorder = input("\n상품을 주문하시겠습니까? (Y/N) : ")
        if Sorder in ['y','Y']:
            return True

def InName():
    while True:
        maxsu = 30
        Isu = int(input("주문하실 수량을 입력해주세요 : "))
        if Isu <= maxsu:
            print(f"주문하실 상품의 수량은 {Isu} 박스(팩)입니다.\n")

            print("="*5 + "주문내역" + "="*5)
            print("상품명".ljust(5),"수량".rjust(7))
            print("{:<5}{:>10}".format(Sname, Isu))
            print("-"*18)
            print("결제가격 : ",list.get(Sname) * Isu)
            print("="*18)
            return Isu
        else:
            print("재고가 부족합니다. 수량을 다시 입력해주세요.")
            
            
list = {'사과': 19900,
        '딸기': 13500,
        '바나나': 6900, 
        '포도': 14800}

information = '''
[상품 리스트]
사과(5kg)    19,900원 딸기(500g)  13,500원
바나나(1.5kg) 6,900원 포도(1.8kg) 14,800원
'''
print(information)
print("\n[현재 주문 가능한 상품]")
for item in list:
    print(item,end = " ")
    print()

while True:
    if endcd == True:
        Bodr = Odr()
        if Bodr == 1:
            while True:
                Sname = input("주문할 상품명을 입력하세요 : ")
                if Sname in list:            
                    print("{} 상품을 선택하셨습니다. 가격은 {:,}원입니다.\n".format(Sname,list.get(Sname)))
                    break
                else:
                    print("존재하지 않거나 주문이 불가능한 상품입니다.")
            
            InName()
            
            while True:
                endorder = input("주문을 완료하시겠습니까? (Y/N) : ")
                if endorder in ['Y','y']:
                    rt = datetime.datetime.now()
                    print("주문 시각은 {}월 {}일 {}시 {}분 입니다.".format(rt.month, rt.day, rt.hour, rt.minute)) 
                    print("주문번호는{}{:0>2}{}{} 입니다.".format(rt.year,rt.month,rt.day,sn))
                    endcd = False
                    break
                elif endorder in ['N','n']:
                    print("주문이 취소되었습니다.")
                    endcd = True
                    break
                else:
                    continue
    else:
        break
