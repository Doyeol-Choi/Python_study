# 클래스 + 상속을 이용한 스타크래프트3
# class_inheritance_starcraft_3
# 상속 : 단일상속(하나로부터 물려받는것), 다중상속(2개 이상의 상위클래스로부터 물려받는것)

# 일반 유닛
class Unit:     # 상위클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
# 공격 유닛
class AttackUnit(Unit):     # 하위클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack('5시')
# 공격을 2번 받는다고 가정
firebat1.damaged(125)
# firebat1.damaged(25)