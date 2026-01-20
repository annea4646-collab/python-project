''' Start() 메소드를 아래의 요구조건을 정의
     - Smartphone 클래스의 인스턴스 생성
     - 사용자로부터 입력을 받아 Addr 인스턴스를 생성해서 Smartphone 클래스의 인스턴스가 가지고 있는 리스트에 추가
     - 리스트에 연락처 정보를 2개 정도 추가해봄
     - 리스트의 모든 요소를 출력
     - 리스트의 모든 요소를 검색
     - 리스트의 요소를 삭제
     - 리스트의 요소를 수정
'''

from SmartPhone import SmartPhone

sp = SmartPhone()


prompt = '''
주소관리 메뉴
------------------
1. 연락처 등록
2. 모든 연락처 출력
3. 연락처 검색
4. 연락처 삭제
5. 연락처 수정
6. 프로그램 종료
------------------ '''

while True:
    print(prompt)
    printMenu=(input("원하는 작업을 선택하세요(1-6): "))

    if printMenu == '1':
        pa = sp.inputAddrData()
        sp.addAddr(pa)

    elif printMenu == '2':
        sp.printAllAddr()

    elif printMenu == '3':
        name = input("검색할 이름을 입력하세요: ")
        sp.searchAddr(name)

    elif printMenu == '4':
        name = input("삭제할 이름을 입력하세요: ")
        sp.deleteAddr(name)       
        
    elif printMenu == '5':
        name = input("수정할 연락처의 이름을 입력하세요: ")
        sp.editAddr(name)

    elif printMenu == '6':
        print("프로그램을 종료합니다.")
        break
    else:
        print("숫자 1 ~ 6 중에 선택하여 입력해주세요.")


