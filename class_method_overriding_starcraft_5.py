# 메소드 오버라이딩 : 부모클래스에 정의한 메소드가 아닌 상속받은 자식클래스에서 새롭게
                # 정의한 메소드를 사용하고자 할 때, 메소드 오버라이딩 이라고 한다.
                # 연산자 오버라이딩이라고도 한다.

# 일반 유닛 name, hp, speed 3개를 매개변수(파라미터)로 하는 생성자
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):   # 지상 유닛의 이동
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
# 공격 유닛 name, hp, speed, damage
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))
        
# 날 수 있는 기능을 가진 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # speed 값이 없으므로 0으로 넣어줌
        Flyable.__init__(self, flying_speed)
        
    # 메소드 오버라이딩 : 상위클래스에서 사용된 메소드를 하위클래스에서 재정의하여 사용하는 기법
                        # 덮어쓰기라고도 한다.
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
# valkyrie.move("3시")

#벌쳐 : 지상 공격 유닛, 스피드가 좋아 기동성이 뛰어남.
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛의 최강! 체력과 공격력 아주 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 벌쳐를 11시 방향으로 이동시키고, 배틀크루저를 9시 방향으로 이동시키세요
vulture.move("11시")
battlecruiser.move("9시")

# 마린(지상 공격), 메딕(의무병) 3시방향으로 이동
marine = AttackUnit("마린", 40, 5, 6)
medic = Unit("메딕", 50, 5)
marine.move("3시")
medic.move("3시")


