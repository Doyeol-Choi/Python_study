# A 학급에 총 10명의 학생이 있다.
# 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 85, 100, 85]

# for문을 이용하여 A 학급의 평균 점수를 출력하시오.
# 반복변수는 score, total: 합계 누정변수, average: 평균변수
# 출력형태 "A 학급의 평균점수는 xx.x점 입니다." (소수 첫째자리까지)

a = [70, 60, 55, 75, 95, 90, 80, 85, 100, 85]
total = 0   # 누적변수는 처음에 초기화 0 을 해주어야 한다.
for score in a:
    total += score
    
average = total / len(a)    # len(a) a 리스트의 요소갯수 10
print("A 학급의 평균점수는 %0.1f점 입니다." % average)