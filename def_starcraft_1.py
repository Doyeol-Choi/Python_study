# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음.add()
# 단순 메소드를 이용한 스타크래프트1
# def_starcraft_1.py
name = "마린"   # 유닛의 이름
hp = 40         # 유닛의 체력
damage = 5      # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력{1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 포를 쏘는데, 두가지 모드 : 일반모드 / 시즈모드(강력해짐)

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
        .format(name, location, damage))    # 백슬래시 \ 코딩 문장이 길 때 다음줄로 개행의미
    
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
    