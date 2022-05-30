# 클래스와 메소드를 이용한 스타크래프트2
# class_def_starcraft_2.py

#클래스이름 : Unit
from unicodedata import name


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'\n{self.name} 유닛이 생성되었습니다.')
        print(f'체력 {self.hp}, 공격력{self.damage}\n')
        
    # def attack(self, location):
    #     print(f'{self.name} : {location}시 방향으로 적군을 공격합니다. [공격력 {self.damage}]')
        
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 적군을 아군으로
wraith2 = Unit("빼앗은 레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith2.name, wraith2.damage))

wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# marine1.attack(1)
# marine2.attack(1)
# tank1.attack(1)   