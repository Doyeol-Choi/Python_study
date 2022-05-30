# if 제어문 실습
# if_1.py

pocket = ['paper', 'cellphone']
card = False
if 'money' in pocket:
    print("일반 택시를 타고 가라")
else:
    if card:
        print("카카오 택시를 타고 가라")
    else:
        print("돈과 카드가 없으니 걸어 가라")