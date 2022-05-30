# 메뉴
def menu():
    print('\n**********************')
    print('* 1. 회원가입        *')
    print('* 2. 회원검색        *')
    print('* 3. 회원탈퇴        *')
    print('* 0. 종료            *')
    print('**********************')
    cho = input('')
    if cho not in ('1','2','3','0'):
        print('잘못된 입력입니다.')
        menu()
    return cho

# 회원가입
def add(db):
    add_id_t = True
    add_pw_t = True
    while add_id_t:
        u_id = input('ID : ')
        if len(u_id) >= 4:
            n = len(db)
            if n != 0:
                for i in range(0,n):
                    if u_id in db[i]:
                        print("이미 존재합니다. 사용할 수 없습니다.")
                        add_id_t = True
                        break
                    else:
                        add_id_t = False
            else:
                add_id_t = False
        else:
            print("아이디는 4글자 이상으로 생성해주세요.")
    while add_pw_t:
        u_pw = input('p/w : ')
        if 6 <= len(u_pw) < 12:
            add_pw_t = False
        else:
            print("비밀번호는 6자 이상 12자 미만으로 생성해주세요.")
    u_name = input('이름 : ')
    u_adr = input('주소 : ')
    u_pho = input('전화번호 : ')
    u_num = input('주민번호 : ')
    u_mail = input('이메일 : ')
    wdb = [u_id, u_pw, u_name, u_adr, u_pho, u_num, u_mail]
    db.append(wdb)
    
# 회원검색메뉴
def serch():
    print('\n******<검색항목>*******')
    print('* 1. ID              *')
    print('* 2. 이름            *')
    print('* 3. 이메일 주소      *')
    print('* 이외. 검색취소      *')
    print('**********************')
    cho = input('')
    return cho

# 회원검색 ID
def serch_id(db):
    n = len(db)
    if n != 0:
        ser_id = input('찾으실 아이디를 입력해주세요. : ')
        con = True
        for i in range(0,n):
            if ser_id == db[i][0]:
                need = db[i][1:]
                print(db[i][0], need)
                con = False
                break
        if con:     # if con == True 와 동일
            print("아이디가 존재하지 않습니다.")
    else:
        print('등록된 회원이 없습니다.')

# 회원검색 이름
def serch_name(db):
    n = len(db)
    if n != 0:
        ser_name = input('찾으실 이름을 입력해주세요. : ')
        con = True   
        for i in range(0,n):
            if ser_name == db[i][2]:
                need = db[i][:2] + db[i][3:]
                print(db[i][2], need)
                con = False
                break
        if con:
            print("이름이 존재하지 않습니다.")
    else:
        print('등록된 회원이 없습니다.')
    
# 회원검색 이메일주소 
def serch_mail(db):
    n = len(db)
    if n != 0:
        ser_mail = input('찾으실 이메일주소를 입력해주세요. : ')
        con = True
        for i in range(0,n):
            if ser_mail == db[i][6]:
                need = db[i][:6]
                print(db[i][6], need)
                con = False
                break
        if con:
            print("이메일이 존재하지 않습니다.")
    else:
        print('등록된 회원이 없습니다.')

# 회원삭제
def delete(db):
    n = len(db)
    if n != 0:
        u_del = input('삭제할 id를 입력하세요. : ')
        for i in range(0,n):
            if u_del == db[i][0]:
                del db[i]
                print(f'ID : {u_del} 가 삭제되었습니다.')
                break
        if n == len(db):
            print("ID가 존재하지 않습니다.")
    else:
        print('등록된 회원이 없습니다.')


# 동작
db = []
while True:
    cho = menu()
    if cho == '1':
       add(db) 
    elif cho == '2':
        cho2 = serch()
        if cho2 == '1':
            serch_id(db)
        elif cho2 == '2':
            serch_name(db)
        elif cho2 == '3':
            serch_mail(db)
        else:
            print('검색을 취소합니다.')
    elif cho == '3':
        delete(db)
    elif cho == '0':
        print("종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")