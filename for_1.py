# while True:
#     print("Ctal + C를 눌러야 WHILE문을 빠져 나갈 수 있습니다.")

"""
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
"""

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue  # < 의 반대기호는 >= 이다.
    print("%d번 학생 축하합니다. 합격입니다." % number)
    
    
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60: continue
#     print("%d번 학생 불합격입니다. 다음기회에 볼게요." % number)