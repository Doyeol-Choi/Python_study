# 다양한 입출력 형식
# """ ~ """ 사이는 다 주석처리
"""
print("Python", "Java", "JavaScript")   # Python Java JavaScript
print("Python", "Java", "JavaScript", sep = "")     # PythonJavaJavaScript
print("Python", "Java", "JavaScript", sep = " Vs ") # Python Vs Java Vs JavaScript
print("Python", "Java", "JavaScript", sep=", ", end="?")    # Python, Java, JavaScript?
print("\n무엇이 더 재미있을까요?")  # end 때문에 윗줄에 붙기 때문에 \n으로 줄바꿈

scores = {"수학" : 0, "영어" : 50, "코딩": 100}  # 딕셔너리
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(3), str(score).rjust(4), sep=":") # 정형화된 포맷
                                                    # ljust 왼쪽정렬, rjust 오른쪽정렬
    
# 은행 대기순번표
# 001, 002, 003, ......add()

for num in range(1, 21):    # 1 ~ 20까지 반복 실행
    print("대기번호 : " + str(num).zfill(3))    # .zfill(3) 3자리의 빈자리를 0으로 채운다.

answer1 = input("첫번째 아무 값이나 입력하세요 : ")
print("입력한 값은 " + answer1 + "입니다.")
print(type(answer1))

answer2 = int(input("두번째 아무 값이나 입력하세요 : "))
# print("입력한 값은 " + str(answer2) + "입니다.")    # 스트링과 숫자형은 연결연산자 사용불가
print(type(answer2))    # 따라서 수치데이터 연산에는 무조건 int 형변환을 해줘야 한다.
# 숫자 타입변환은 int, 문자 타입변환은 str
"""

# 10자리 확보하고, 빈자리는 빈공간으로 두고, 오른쪽 정렬하라.
print("{0:>10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0:>+10}".format(500))  # 위에선 +는 보이지 않지만 이건 +, - 가 다 표시됨
print("{0:>+10}".format(-500))

# 왼쪽 정렬하고, 나머지는 _로 채움
print("{0:_<+10}".format(500))
print("{0:,>+10}".format(500))  # 콤마 위치에 따라 3자리 콤마와 콤마 채우기 달라짐

# 3자리마다 콤마
print("{0:,}".format(1000000000))
# 3자리마다 콤마하고 부호(+,-)도 붙이고
print("{0:+,}".format(-1000000))
print("{0:-,}".format(-1000000))

# 빈자리는 ^ 로 채워주기, 왼쪽정렬, 3자리 콤마
print("{0:^<+20,}".format(1000000))

# 소수점 출력
print("{0:f}".format(5/3))  # 소수점 6자리까지 출력 뒤는 반올림

# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))   # 소수점 셋째자리에서 반올림
