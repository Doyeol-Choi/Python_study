# 결과값이 없는 함수

# def profile(name, age, address):
#     print("나의 이름은 %s이고, 나이는 %d이고, 주소는 %s입니다." \ 
#           % (name, age, address))
    
# print(profile(a, 20, b))

def profile(name, age, address):
    print("나의 이름은 {0}이고, 나이는 {1}이고, 주소는 {2}입니다."\
        .format(name, age, address))     # \ 는 에러 없이 줄바꾸기.

# name = input("이름을 입력하세요>> ")
# age = int(input("나이를 입력하세요>> "))
# address = input("주소를 입력하세요>> ")    
# print(profile(name, age, address))

print(profile(input("이름을 입력하세요>> "), int(input("나이를 입력하세요>> ")), input("주소를 입력하세요>> ")))