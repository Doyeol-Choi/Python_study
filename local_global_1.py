# local : 지역변수
# global : 전역변수


# area가 지역변수로 사용, 지역변수는 함수내에서만 사용되고, 함수밖으로 나가면 소멸된다.
def circle_area():
    area = 3.14 * radius ** 2       # ** 2 는 제곱
    print(area)
    return area

area = 0
print(area)
radius = float(input("반지름을 입력하세요>> "))
print(area)
print("원의 넓이: ", circle_area())
print(area)     # 함수 내에서 area값을 사용하고 함수가 끝나고 나면 clear 된다.

# 함수내에서 사용한 area는 local(지역변수)이고
# 함수 밖에서도 사용가능한 area는 global(전역변수)


# 전역변수 global, 함수 밖에서도 공유하여 사용가능. 
# 실무에서는 global을 안씀. 제한을 두는게 더 좋음.

def circle_area():
    global area
    area = 3.14 * radius ** 2
    print(area)
    return area

area = 0
print(area)
radius = float(input("반지름을 입력하세요>> "))
print(area)
print("원의 넓이: ", circle_area())
print(area)