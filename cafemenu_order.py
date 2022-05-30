menu = { 'Americano':3000, 'Ice Americano':3500, 'Cappuccino':4000, 'Cafe Latte':4500, 'Espresso':3600}

# for coffee in menu:
#     print("{:<15} 가격 : {}원".format(coffee, menu.get(coffee)))

for coffee, price in menu.items():
    print("{:<15} 가격 : {}원".format(coffee, price))   
    # {:<15} 값이 15칸 보다 작더라도 공백으로 15칸을 채운다. 값이 15칸 이상이면 차이없음
    # {:>15} <, > 에 따라 정렬 방향이 달라짐 < 왼쪽, > 오른쪽

order = input("\n위의 메뉴중 하나를 선택해주세요 : ")
if order in menu:
    print("주문하신 {0}는 {1}입니다. 결제를 부탁드립니다.".format(order, menu.get(order)))
else:
    print(f"미안합니다. {order}는 메뉴에 없습니다.")