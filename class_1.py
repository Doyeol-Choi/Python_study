class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
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
    
    def mod_c(self):
        result = self.first % self.second
        return result
    
# 클래스를 정의했으면 먼저 객체를 생성한다. ==> 인스턴스화
a = FourCal()   # FourCal 클래스의 인스턴스
c = int(input("첫번째 숫자를 입력하세요> "))
d = int(input("두번째 숫자를 입력하세요> "))
a.setdata(c, d)
print("a + b =", a.add())
print("a - b =", a.sub())
print("a * b =", a.mul())
print("a / b =", a.div())
print("a % b =", a.mod_c())
