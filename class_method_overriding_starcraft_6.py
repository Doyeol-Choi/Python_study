# 마린 3기, 탱크 2기, 레이스 1기를 생성하여 전군 1시 방향으로 공격개시!

# 일반 유닛

import random

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        
    def move(self, location):   # 지상 유닛 이동 메소드
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]"\
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # speed = 지상유닛의 속도
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):   # 메소드 오버라이딩
        self.fly(self.name, location)
        
# 레이스
class Wratith(FlyableAttackUnit):
    clock_developed = False
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False    # 클로킹 모드 : 해제 상태
        
    def clocking(self):
        if Wratith.clock_developed == True:
            if self.clocked == True:    # 클로킹 모드 -> 해제
                print("{0} : 클로킹 모드 해제합니다.".format(self.name))
                self.clocked = False
            else:
                print("{0} : 클로킹 모드 합니다.".format(self.name))
                self.clocked = True
                
        else:
            print("[알림] 클로킹 모드가 개발되지 않았습니다.")
            
            
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def steampack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)"\
                .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다."\
                .format(self.name))
            
# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격이 가능한 모드, 이동은 불가!
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
        
        
    def set_seize_mode(self):
        if Tank.seize_developed == True:
            if self.seize_mode == False:
                print("{0} : 시즈모드로 전환합니다.".format(self.name))
                self.speed = 0
                self.damage *= 2
                self.seize_mode = True
                
            else:
                print("{0} : 시즈모드를 해제합니다.".format(self.name))
                self.speed = 1
                self.damage /= 2
                self.seize_mode = False
        
        else:
            print("[알림] 시즈모드가 개발되지 않았습니다.")
            
# def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_developed == False:
#             print("{0} : 시즈모드로 전환합니다\n".format(self.name))
#             self.damage *= 2
#             self.set_seize_mode = True
            
#         else: # 현재 시즈모드 일 때 -> 시즈모드 해제
#             print("{0} : 시즈모드를 해제합니다.\n".format(self.name))
#             self.damage /= 2
#             self.set_seize_mode = False
            
            

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg")
    print("[Player] 님이 퇴장하셨습니다.")
    

game_start()

marine1=Marine()
marine2=Marine()
marine3=Marine()

tank1=Tank()
tank2=Tank()

wraith1=Wratith()

attack_units=[]
attack_units.append(marine1)        # a.append(b) b를 a(list)에 넣어라
attack_units.append(marine2)
attack_units.append(marine3)
attack_units.append(tank1)
attack_units.append(tank2)
attack_units.append(wraith1)

for unit in attack_units:
    unit.move("1시")
    
Tank.seize_developed = True
print("[알림] 시즈탱크 유닛의 시즈모드 개발이 완료되었습니다.")
Wratith.clock_developed = True
print("[알림] 레이스의 유닛의 은신 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):        # isinstance(1, int) 1이 인트형 인지 확인하는 함수
        unit.steampack()
    elif isinstance(unit, Tank):        # 여기에선 unit이 Tank 인지 확인하는 함수로 사용
        unit.set_seize_mode()
    elif isinstance(unit, Wratith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")
    
for unit in attack_units:
    unit.damaged(random.randint(20, 100)) #20~100까지 랜덤하게 발생
    
game_over()