# 영화 예매 하기

# 해당되는 리스트(movies)의 목록의 영화명을 선택하면,
# 관람인원을 선택하게 하고,
# 할인권이 있으면, y를 선택하고, 할인쿠폰 코드를 입력하면
# 할인 금액이 적용된 청구금액을 출력해준다.

movies = ["스파이더맨", "아바타2", "기생충", "타이타닉", "클래식"]

print("\n========영화 목록========")
for item in movies:
    print(item)
print("========영화 목록========\n")

choice = input("예매하실 영화명을 입력하세요. : ")

while choice not in movies:
    print("\n예매할 수 없는 영화입니다.\n")
    choice = input("예매하실 영화명을 입력하세요. : ")
    
print("\n예매하실 영화를 선택해주세요 : ", choice, "을(를) 선택하셨습니다.\n")

check = False
while (not check):  # not check로 check를 True로 입력
    people = int(input("\n관람하실 인원을 입력하세요 : "))
    if people < 1:
        print("\n관람 인원 수는 한 명 이상입니다.")
    else:
        print("\n관람할 인원수는 %d명 입니다." % people)
        check = True    # 위가 not check 이기때문에 True로 바꿔줘야 while 탈출

coupon_dic = {'WELCOME':1000, 'VALENTINE':2000, 'CHRISTMAS':3000, 'EVENTDAY':4000}
process = True
# print("\n할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요:")
usage = input("\n할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요 : ")
while process:  # break로 멈춰서 그냥 True나 1로 넣어도 될 것 같음
    if (usage == 'y') or (usage == 'Y'):
        coupon = input("\n쿠폰코드를 입력해주세요. : ")
        if coupon in coupon_dic:
            sale = coupon_dic[coupon]   # coupon_dic[coupon] key값에 해당하는 value 값 출력
            print("\n%d원 할인됩니다." % sale)
            break
        elif (usage == 'n') or (usage == 'N'):
            sale = 0
            print("\n할인권을 사용하지 않았습니다.")
            break
        else:
            print("\n존재하지 않는 할인권입니다.")
            usage = input("\n할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요 : ")
            while usage not in ['Y','y','N','n']:
                usage = input("\n잘못된 입력입니다. 다시 입력해주세요 (y/n) : ")
    elif (usage == 'n') or (usage == 'N'):
        sale = 0
        print("\n할인권을 사용하지 않았습니다.")
        break
    else:
        usage = input("\n잘못된 입력입니다. 다시 입력해주세요 (y/n) : ")
        
origin_price = 12000
sale_price = sale
total_price = (origin_price - sale_price) * people

print("\n<예매 상세 내역>")
print("="*24)
print("영화 제목 : %s" % choice)
print("관람 인원 : %d명" % people)
print("관람 금액 : %d원" % origin_price)
print("할인 금액 : %d원" % sale_price)
print("-"*24)
print("청구 금액 : %d원" % total_price)
print("="*24)

