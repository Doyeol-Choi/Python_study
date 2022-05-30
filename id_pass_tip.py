def menu_input():
    print('*********************')
    print('* 1. 회원가입       *')
    print('* 2. 회원검색       *')
    print('* 3. 회원탈퇴       *')
    print('* 0. 종료           *')
    print('*********************')
    return int(input())

#입력
def member_input():
    #아이디 입력
    mid=''
    while len(mid)<4:
        mid=input('ID: ')
        if mid in member:
            print('이미 존재하는 ID 입니다')
            mid=''
    #패스워드 입력        
    passw=''
    while len(passw)<6 or len(passw)>12 :
        passw=input('p/w: ')
    mem=[passw]
    # 이름,주소,전화,주민 이메일 입력
    for i in range(1,6):
        mm=input(hang[i]+': ')
        mem.append(mm)
    member[mid]=mem

#검색
def member_surch():
    print('*****<검색항목>******')
    print('* 1. ID             *')
    print('* 2. 이름           *')
    print('* 3. 이메일 주소    *')
    print('* 이외. 검색최소    *')
    print('*********************')
    ny = int(input())
    if ny==1:    # iD 검색이면 찾을 아이디에 입력분을 저장
        sid=input('찾을 id를 입력하세요.')
    else:
        if ny==2: 
            sp=1
        elif ny==3:
            sp=5
        else:
            return

        # id찾기가 아니면 해당 항목을 찾아  아이디에 찾은 아이디 저장
        sid=None
        smm=input('찾을 '+'hang[sp]'+'를 입력하세요.')
        for i in member:
            if member[i][sp]==smm:
                sid=i
                break

    if sid in member:
        print(sid,member[sid])
    else:
        print('찾으시는 화원이 없습니다.')

#삭제
def member_del():
    did=input('삭제할 id를 입력하세요. ')
    if did in member:
        del member[did]
        print('ID: '+did,'가 삭제 되었슴니다.')
    else:
        print('찾으시는 화원이 없습니다.')
    
#본 프로그램
hang=['비밀번호','이름','주소','전화번호','주민번호','이메일']
member={}
menu=menu_input()
while menu!=0:
    if menu==1:
        member_input()
    elif menu==2:
        member_surch()
    elif menu==3:
        member_del()
    menu=menu_input()

print(member)


# 0. 회원가입, 회원 검색, 회원 탈퇴 등의 기능을 선택할 수 있는 메뉴를 구성하여 각 메뉴를 선택하면 필요한 기능을 수행하도록 한다.
# 1. 회원가입시 이름, 아이디, 비밀번호, 주소, 전화번호, 주민등록번호, 이메일 주소를 입력받는다.
# 2. 아이디는 영문과 숫자로 이루어져 있어야 하고, 비밀번호는 영어, 숫자, 특수문자를 섞어서 사용해야 한다.
# 3. 아이디는 최소 4자 이상이어야 하고, 비밀번호는 6자에서 12자 사이여야 함.
# 4. 동일한 아이디 가입은 불가한다.
# 5. 아이디가 중복되거나 비밀번호가 규칙에 맞지 않으면 맞을때까지 계속 입력받도록 한다.
# 6. 회원 가입이 끝나면 최초 메뉴 화면으로 돌아가도록 한다.
# 7. 회원 검색은 이름이나, 아이디, 이메일 주소로 검색할 수 있도록 한다.
# 8. 회원 탈퇴는 검색된 사용자넣으면 리스트에서 삭제하도록 한다.