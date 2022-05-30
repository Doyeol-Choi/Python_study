# 상위클래스

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 메소드가 호출되었습니다.")  # 1번
        
    def test(self):
        print("Parent 클래스의 test 메소드가 호출되었습니다.")      # 2번
        
# 하위 클래스 선언

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)   # Child 클래스가 Parent 클래스를 상속하지 않았다면 __init__ 메소드만 호출해서 사용했기때문에 __init__만 사용 가능하다.
        print("Child 클래스의 __init__메소드가 호출되었습니다.")    # 3번
        
    def test(self):
        print("Child 클래스의 test() 메소드가 호출되었습니다.")     # 4번
        
        
a = Child()
a.test()    # test() 부모 메소드인데, a 객체는 자식클래스의 객체임에도 상속(Inheritance)을 했기 때문에 호출이 가능하다.
print(a.value)

# 실행순서 번호 => 1 / 3 / 2 / 테스트

b = Parent()    # 만약 Child 클래스가 Parent 클래스를 상속하지 않았다면 b.test만 출력 가능하다.
b.test()

# __init__ 의 이해
# - 생성자(컨스트럭터)라고 불리는 초기화를 위한 특수한 메소드(함수)
# - 인스턴스화를 실시할 때 반드시 처음에 호출되는 특수한 함수
# - 오브젝트 생성(인스턴스 생성)과 관련하여 데이터의 초기를 실시하는 함수
# - __init__()은 반드시 첫번째 인수로 self로 지정해야 한다. self에는 인스턴스 자체가 전달된다.