# if ~ elif ~ else 를 이용해 학점계산 만들기
# score.py

score = int(input("점수를 입력하세요?>> "))

if score >= 90:
    print("학점은 A학점 입니다.")
elif score >= 80:
    print("학점은 B학점 입니다.")
elif score >= 70:
    print("학점은 C학점 입니다.")
elif score >= 60:
    print("학점은 D학점 입니다.")
else:
    print("학점은 F학점 입니다.")