class FourCal:
    def setdata(self, first, second):
        self.first = first         # self.first는 setdata의 변수 뒤의 first는 매개변수
        self.second = second       # self 대신 다른 문자여도 상관없으나 실무에선 self사용
        
    def add(self):
        result = self.first + self.second       # 위의 setdata의 변수를 가져다 사용
        return result
    
a = FourCal()
a.setdata(4, 2)
print(a.add())