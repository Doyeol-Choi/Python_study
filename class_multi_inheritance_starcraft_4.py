# 일반 유닛
class Unit:
    def __init__(self, name, hp):   # 자동 호출되는 생성자(역할: 객체 생성시(인스턴스화) 빠르게 초깃값 부여)
        self.name = name    # 멤버변수
        self.hp = hp
        
# 공격 유닛
class AttackUnit(Unit):     # Unit 클래스를 단일 상속
    def __init__(self, name, hp, damage):   # 3개의 매개변수로 전달 => 인스턴스화 할때
        Unit.__init__(self, name, hp)   # 부모클래스 Unit 호출, 인수값 두 개 가지고 전달
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
# 드랍쉽 : 공중 유닛, 수송기 역할, 마린/파이어뱃/탱크 등을 수송하는 것만, 공격 기능 불가!

# 날 수 있는 기능을 가진 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
        
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):   # 다중 상속 AttackUnit이 이미 Unit을 상속받았기 때문에 Unit 역시 상속받는다.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkrie1 = FlyableAttackUnit("발키리", 200, 6, 5)
valkrie1.fly(valkrie1.name, "3시")
valkrie1.attack("3시")
valkrie1.damaged(120)
valkrie1.damaged(120)

