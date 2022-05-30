# Student 클래스를 선언

class Student:  # 클래스는 첫 글자 대문자, 합성 단어 각각 대문자 FourCal 클린코드 => 가독성 높이기 위함.
    count = 0   # 클래스 변수
    
    def __init__(self, name, korean, math, english, science):   # 매개변수
        # 인스턴스 초기화
        self.name = name    # self.name => 맴버변수, name => 매개변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    # 클래스변수 카운트 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))
        
# 학생 list 선언

students = [        # [] 리스트, () 튜플, {} set(집합), 딕셔너리
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 82, 92)
]
