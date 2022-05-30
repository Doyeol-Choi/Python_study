# Student 클래스를 선언

class Student:  # 클래스는 첫 글자 대문자, 합성 단어 각각 대문자 FourCal 클린코드 => 가독성 높이기 위함.
    # count = 0   # 클래스 변수
    
    def __init__(self, name, korean, math, english, science):   # 매개변수
        # 인스턴스 초기화
        self.name = name    # self.name => 맴버변수, name => 매개변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    def get_sum(self):  # 합계 구하기
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):  # 평균 구하기
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
        
# 학생 list 선언

students = [        # [] 리스트, () 튜플, {} set(집합), 딕셔너리
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 82, 92)
]

# 학생을 한 명씩 출력하겠습니다.

print("이름", "총점", "평균", sep='\t')     # sep 앞의 각 값 사이마다 특정데이터 넣기
for student in students:
    print(str(student))
    
