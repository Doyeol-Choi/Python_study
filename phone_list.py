# 전화번호부 관리

print("전화번호 저장, 전체보기")

phone_list = []
while True:
    sel_ch = input("\n전체보기(0), 저장(1), 삭제(2), 끝내기(3) : ")
    if sel_ch == '0':
        temp = sorted(phone_list)
        for list in temp:
            print(list)
    elif sel_ch == '1':
        add_name = input("저장이름 : ")
        add_phone = input("전화번호 : ")
        if len(add_name) != 0 and len(add_phone) != 0:      # null 일때 다시 입력받도록
            phone_list.append([add_name,add_phone])
        else:
            print("다시입력해주세요.")
    elif sel_ch == '2':
        count = 0
        del_name = input("삭제할 이름 : ")
        while True:
            if del_name in phone_list[count]:
                phone_list.pop(count)
                break
            elif count == (len(phone_list)-1):      # len이 6일때 count는 5까지
                print("존재하지 않습니다.")
                break
            else:
                count += 1
    elif sel_ch == '3':
        re = input("정말로 끝내시겠습니까? (y/n) : ")
        if re in ['y','Y']:
            print("종료합니다.")
            break

    else:
        print("잘못입력하셨습니다.")
    
    # else:
    #     re = input("정말로 끝내시겠습니까? (y/n) : ")
    #     if re in ['y','Y']:
    #         print("종료합니다.")
    #     else:
    #         continue              # continue 알아두기
    #     break