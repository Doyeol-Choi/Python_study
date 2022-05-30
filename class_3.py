class Person:
    total_count = 0     # total_count 클래스변수(=속성, 데이터, 필드)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # total_count += 1    # 에러. 클래스변수에 접근할때에는 반드시 클래스명.클래스변수
        Person.total_count += 1
    def introduce(self):
        print(f'나의 이름은 {self.name}이고, 나이는 {self.age}살 입니다.')
        
# p1~p6 인조로봇 생성
p1 = Person('최도열', 32)
p2 = Person('일이삼', 17)
p3 = Person('사오육', 34)
p4 = Person('칠팔구', 18)
p5 = Person('십십일', 36)
p6 = Person('십이삼', 54)
print("Person 클래스로부터 객체가 생성되고 있습니다.")
# 각 객체를 출력해주세요
p1.introduce()
p2.introduce()
p3.introduce()
p4.introduce()
p5.introduce()
p6.introduce()

print(f'우리반은 모두 {Person.total_count}명 입니다.')
print(f'우리 {Person.total_count}명의 클래스는 모두 Person 입니다.')

