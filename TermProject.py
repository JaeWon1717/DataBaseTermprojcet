##code 
def print_covid(rows):
    print("\n----------------------------------------------------------------------------------------------------------------")
    cnames = ['학번', '이름', '호실', '감염경로', '귀가여부','확진날짜']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n----------------------------------------------------------------------------------------------------------------")
    ccodes = ['StuID', 'Name', 'Room', 'route', 'hmc','date']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("----------------------------------------------------------------------------------------------------------------")
def print_Sleepover(rows):
    print("\n------------------------------------------------------------------------")
    cnames = ['학번', '이름', '호실', '신청날짜', '신청사유']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n------------------------------------------------------------------------")
    ccodes = ['StuID', 'Name', 'Room', 'Date', 'reason']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("------------------------------------------------------------------------")
def print_NewDom(rows):
    print("\n------------------------------------------------------------------------")
    cnames = ['학번', '이름', '전공', '학년', '호실']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n------------------------------------------------------------------------")
    ccodes = ['StuID', 'Name', 'Major', 'Grade', 'Room']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("------------------------------------------------------------------------")
def print_New(rows):
    print("\n------------------------------------------------------------------------")
    cnames = ['학번', '이름', '전공', '학년']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n------------------------------------------------------------------------")
    ccodes = ['StuID', 'Name', 'Major', 'Grade']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("------------------------------------------------------------------------")
def print_meritTable(rows):
    print("\n--------------------------------------------------")
    cnames = ['학번', ' 상점', '벌점']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n--------------------------------------------------")
    ccodes = ['StuID', 'merit', 'demerit']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("--------------------------------------------------")
def print_merit(rows):
    print("\n--------------------------------------------------")
    cnames = ['학번', ' 상점']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n--------------------------------------------------")
    ccodes = ['StuID', 'merit']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("--------------------------------------------------")
def print_demerit(rows):
    print("\n--------------------------------------------------")
    cnames = ['학번','벌점']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n--------------------------------------------------")
    ccodes = ['StuID','demerit']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("--------------------------------------------------")
def print_Menu(rows):
    print("\n------------------------------------------------------------------")
    cnames = ['날짜','밥','반찬','국']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n------------------------------------------------------------------")
    ccodes = ['Date','Rice','side','soup']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("------------------------------------------------------------------")
def print_Domnum(rows):
    print("\n------------------------------------------------------------------------")
    cnames = ['학번', '호실']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n------------------------------------------------------------------------")
    ccodes = ['StuID', 'Room']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("------------------------------------------------------------------------")
def print_Repair(rows):
    print("\n--------------------------------------------------")
    cnames = ['호실', ' 요구사항']
    for c in cnames:
        print(c.center(11, ' '), end='\t')
    print("\n--------------------------------------------------")
    ccodes = ['Room', 'Repair']
    for r in rows:
        for c in ccodes:
            print(str(r[c]).center(11, ' '), end='\t')
        print("")
        print("--------------------------------------------------")
import pymysql

connect = pymysql.connect(host='192.168.230.3',user='jpark', password='1234', db='Termpro', port=4567, charset='utf8',)


cur = connect.cursor(pymysql.cursors.DictCursor)

a='na' 
while a !=999:
            print('\n\n')
            print('********************')
            print('1. 입주신청 \n')#완성
            print('2. 기숙사 호실 신청하기 \n') #완성 
            print('3. 관원생조회 \n') #완성
            print('4. 외박신청하기\n') #완성 
            print('5. 코로나19확진신고\n')#완성
            print('6. 상벌점 조회\n')#완성
            print('7. 급식 메뉴 조회하기\n')#완성
            print('8. 유지보수 접수하기\n')
            print('9. 관리자용: 전체테이블조회\n')
            print('999.저장하고 나가기\n')
            print('입력된 번호 : ')
            print('********************')

            a=int(input())        
            if a == 1:#완성 입주하기 테이블 
                print('입주신청하기')                
                print('입주 하시겠습니까?\n')
                print('1. 입주하기\n')
                print('2. 돌아가기\n')   
                print('테이블 번호를 입력하세요: ')
                table= input()
                if table=='1':
                    print('학번,이름,학과,학년을 순서대로 입력하세요\n')
                    Stuid=input('학번 : ')
                    name=input('이름: ')
                    major=input('학과: ')
                    grade=input('학년: ')
                    sql = "INSERT INTO New VALUES(%s, %s, %s, %s)"       
                    vals = (Stuid,name,major,grade)
                    print('학번:%s\n 이름: %s\n 학과: %s\n 학년: %s\n 입주신청되었습니다! \n'%vals)
                elif table=='2':         
                    print('돌아가기\n')
                elif table=='3':
                    print('이름,학과,학년,학번을 순서대로 입력하세요\n')
                    name=input('이름: ')
                    major=input('학과: ')
                    grade=input('학년: ')
                    StuID=input('학번 : ')
                    sql = "UPDATE New SET Name=%s,Major=%s,Grade=%s where StuID=%s"       
                    vals = (name,major,grade,StuID)                    
                             
                else:
                    print('잘못된 입력입니다.')
                    
                cur.execute(sql, vals)
                connect.commit()
            elif a ==2: #완성 호실등록하기
                print('호실등록하기') 
                print('호실을 선택하시겠습니까?\n')
                print('1. 선택하기\n')
                print('2. 돌아가기\n')   
                print('테이블 번호를 입력하세요: ')
                table= input()
                if table=='1':
                    print('선택호실,학번을 순서대로 입력하세요\n')
                    room=input('선택호실: ')        
                    Stuid=input('학번 : ')
                    sql = "INSERT INTO Dom VALUES(%s, %s)"       
                    vals = (room,Stuid)
                    print('%s 호로 학번: %s  배정되었습니다\n'%vals)
                    cur.execute(sql, vals)
                    connect.commit() 
                elif table=='2':         
                    print('돌아가기\n')                   
                else:
                    print('잘못된 입력입니다.')               
                               
            elif a ==3: #완성 #관원생조회 테이블
                print('전체 관원생조회하기')
                print('검색할 테이블을 선택하세요\n')
                print('1.조회하기\n')
                print('2.돌아가기\n')    
                print('테이블 번호을 입력하세요: ')
                table= input()
                if table=='1':
                    cur.execute("SELECT * FROM New")
                    rows = cur.fetchall()
                    print_New(rows)
                elif table=='2':
                    print('메인메뉴로 돌아갑니다\n')
            elif a ==4:#완성 외박신청테이블
                print('외박신청하기')
                print('외박을 신청하시겠습니까?(입주생만 신청할 수 있습니다)\n')
                print('1. 신청하기\n')    
                print('2. 돌아가기: ')
                table= input()

                if table=='1':
                    print('학번,호실,신청날짜,신청사유를 순서대로 적으세요\n')
                    StuID=input('학번')
                    room=input('호실')
                    date=input('신청날짜')
                    reason=input('신청사유')
                    sql = "INSERT INTO Sleepover VALUES(%s, %s, %s, %s)"       
                    vals = (StuID,room,date,reason)
                    print('학번: %s\n 호실: %s\n 신청날짜 %s\n 신청사유 %s\n 저장되었습니다! \n'%vals)

                elif table=='2':
                    print('돌아가기.')                   
                else:
                    print('잘못된 입력입니다.')                    
                cur.execute(sql, vals)
                connect.commit()
            elif a ==5:#완성 코로19확진 신고 테이블
                print('코로나19확진신고')
                print('코로나 19 확진자 신고하기 (입주생만 신청할 수 있습니다)\n')
                print('1. 신고하기\n')    
                print('2. 돌아가기: ')
                table= input()
                if table=='1':
                    print('학번,호실,이름,감염경로,검사일자,자택귀가 여부를 순서대로 적으세요\n')
                    StuID=input('학번')
                    name=input('이름')
                    room=input('호실')
                    route=input('감염경로')
                    hmc=input('자택귀가여부')
                    date=input('검사일자')
                    sql = "INSERT INTO Covid VALUES(%s, %s, %s, %s, %s, %s)"       
                    vals = (StuID,name,room,route,hmc,date)
                    print('학번: %s\n 이름 %s\n 호실 %s\n 감염경로 %s\n 자택귀가여부 %s\n 검사일자 %s 저장되었습니다! \n'%vals)

                elif table=='2':
                    print('돌아가기.')                   
                else:
                    print('잘못된 입력입니다.')                   
                cur.execute(sql, vals)
                connect.commit()
            elif a ==6:#완성 상벌점 조회 테이블 
                #print('상벌점 조회')
                print('상점,벌점 관리하기 ')
                print('1.상점조회 ')
                print('2.벌점조회 ')
                print('3.상,벌점 전체조회')
                print('4.상점,벌점 부여하기')
                table= input()
                if table=='1': #상점조회
                    merit1 = int(input("몇 점 이상을 검색하시겠습니까? "))
                    merit2 = int(input("몇 점 이하을 검색하시겠습니까? "))
                    a1 =  merit1
                    a2 =  merit2
                    sql = "SELECT * FROM RewardPoints WHERE LEFT(merit, 4) BETWEEN {} AND {}".format(a1,a2)
                    cur.execute(sql)
                    rows = cur.fetchall()
                    print_merit(rows)
                elif table=='2':  #벌점 조회    
                    demerit1 = int(input("몇 점 이상을 검색하시겠습니까? "))
                    demerit2 = int(input("몇 점 이하을 검색하시겠습니까? "))
                    a1 =  demerit1
                    a2 =  demerit2
                    sql = "SELECT * FROM RewardPoints WHERE LEFT(merit, 4) BETWEEN {} AND {}".format(a1,a2)
                    cur.execute(sql)
                    rows = cur.fetchall()
                    print_demerit(rows)  
                elif table=='3':
                    cur.execute("SELECT * FROM RewardPoints")
                    rows = cur.fetchall()
                    print_meritTable(rows)
                elif table=='4':                   
                    print('상점,벌점,학점을 순서대로 입력하세요\n')                    
                    merit=input('상점:')
                    demerit=input('벌점:')
                    StuID=input('학번:')                    
                    sql = "UPDATE RewardPoints SET merit =(%s),demerit=(%s) where StuID=(%s)"      
                    vals = (merit,demerit,StuID)
                    cur.execute(sql, vals)
                    connect.commit()
                    print('학번:%s\n상점:%s\n벌점:%s\n 부여되었습니다! \n'%vals)
                else:
                    print('잘못된 입력입니다.')                   
            elif a ==7:#급식 조회테이블
                print('급식을 조회하시겠습니까?\n')
                print('1. 조회하기\n')
                print('2. 나가기\n')
                table= input()
                if table=='1':
                    cur.execute("select * from Menu")
                    rows = cur.fetchall()
                    print_Menu(rows)         
                elif table=='2':
                    print('돌아가기.')                   
                else:
                    print('잘못된 입력입니다.')
            elif a ==8:#유지보수 신청 테이블
                print('유지보수요청을 등록하시겠습니까??\n')
                print('1. 조회하기\n')
                print('2. 나가기\n')
                table= input()
                if table=='1':
                    print('선택호실,요구사항을 순서대로 입력하세요\n')
                    room=input('선택호실: ')        
                    Repair=input('요구사항(15자 이내) : ')
                    sql = "INSERT INTO Repair VALUES(%s, %s)"       
                    vals = (room,Repair)
                    print('%s 호: %s  접수되었습니다.\n'%vals)
                    cur.execute(sql, vals)
                    connect.commit()         
                elif table=='2':
                    print('돌아가기.')                   
                else:
                    print('잘못된 입력입니다.')
            elif a==9:#9. 관리자용: 전체테이블조회 완성
                print('관리자용메뉴\n')
                print('수행하실 업무를 선택하세요\n')
                print('1. 관원생 조회(호실등록까지 마쳐야 조회가능합니다)\n')
                print('2. 외박신청 현황\n')
                print('3. 코로나 19 감염자 현황\n')
                print('4. 특정호실 조회\n')
                print('5 전체 관원생 수 조회\n') 
                print('6.관원생 호실 이동\n')  
                print('7.유지보수 접수건 확인\n')
                print('8.유지보수 접수건 처리하기')             
                print('테이블 번호을 입력하세요: ')
                table= input()
                if table=='1':
                    cur.execute("select * from New inner join Dom on New.StuID=Dom.StuID")
                    rows = cur.fetchall()
                    print_NewDom(rows)         
                elif table=='2':
                    cur.execute("SELECT * FROM Sleepover")
                    rows = cur.fetchall()
                    print_Sleepover(rows) 
                elif table=='3':
                    cur.execute("SELECT * FROM Covid")
                    rows = cur.fetchall()
                    print_covid(rows)
                elif table=='4':
                    Domnum1 = int(input("몇 호부터 검색하시겠습니까? "))
                    Domnum2 = int(input("몇 호까지 검색하시겠습니까? "))
                    a1 =  Domnum1
                    a2 =  Domnum2
                    sql = "SELECT * FROM Dom WHERE LEFT(Room, 4) BETWEEN {} AND {}".format(a1,a2)
                    cur.execute(sql)
                    rows = cur.fetchall()
                    print_Domnum(rows)
                elif table=='5':
                    sql='select count(*) from New'
                    cur.execute(sql)
                    rows = cur.fetchall()
                    print('전체 관원생 수는')
                    print(rows)
                    print('명 입니다')
                elif table=='6':#관원생 호실이동 
                    print('이동할 방번호와 학번을 입력하세요.(코로나 감염자,외박중인학생은 이용할수없습니다)\n')
                    Room=input('이동할 방번호: ')
                    StuID=input('학번: ')
                    sql = "UPDATE Dom SET Room=%s where StuID=%s"       
                    vals = (Room,StuID)
                    cur.execute(sql, vals)
                    connect.commit()
                elif table=='7':#유지보수 접수사항 확인
                    cur.execute("SELECT * FROM Repair")
                    rows = cur.fetchall()
                    print_Repair(rows)
                elif table =='8':#유지보수 접수건 처리하기
                    print('몇 호를 수리하셨습니까?(기존 유지보수 접수건만 삭제가능)\n')                    
                    room=input('선택호실: ')    
                    sql = "delete from Repair where Room=%s"
                    vals = (room)
                    cur.execute(sql, vals)
                    connect.commit()
                    # rows = cur.fetchall()
                    # print_Domnum(rows)
                else:
                    print('잘못된 입력입니다.')                         
            elif a==999:
                connect.commit()
                print('프로그램을 종료합니다.')
            else:
                print('잘못된 명령어가 입력되었습니다. 다시 입력해주세요')
                