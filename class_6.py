# 상속과 메소드 오버라이딩(Method Overriding)
# class_6.py

class FourCal:  # FourCal 상위클래스, 슈퍼클래스, 부모클래스
    # 상속 : 상위클래스(부모클래스)의 속성, 생성자, 메소드 등을 물려 받아 
    #       하위클래스(자식클래스)에서 사용할 수 있는 기능이다.
    def __init__(self, first, second):  #생성자
        self.first = first  # 멤버변수
        self.second = second
        
    def add(self):  # 메소드
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
class MoreFourCal(FourCal):     # ()괄호 안에 부모클래스를 써주면 자식클래스 생성완료
    def div(self):  # 메소드 오버라이딩 : 상위클래스의 특정 메소드를 하위클래스에서 재정의 한다.
                    # 오버라이딩(덮어쓰기) : 동일한 메소드 이름으로 작성한다. 내용만 바꾼다.
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# a = FourCal(4, 2) 기존 클래스방식, 생성자 호출 ==> __init__ 생성자가 가서 초깃값 부여한다.

# a = FourCal(4, 0)  # 상위클래스에선 div에 self.second가 0으로 나눠져서 에러가 나온다.
a = MoreFourCal(4, 0)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())  # 메소드 오버라이딩 하면 부모 클래스의 div()가 아닌 자식클래스의 div()로 출력한다.


