''' Start() 메소드를 아래의 요구조건을 정의
     - Smartphone 클래스의 인스턴스 생성
     - 사용자로부터 입력을 받아 Addr 인스턴스를 생성해서 Smartphone 클래스의 인스턴스가 가지고 있는 리스트에 추가
     - 리스트에 연락처 정보를 2개 정도 추가해봄
     - 리스트의 모든 요소를 출력
     - 리스트의 모든 요소를 검색
     - 리스트의 요소를 삭제
     - 리스트의 요소를 수정
'''

from SmartPhone import SmartPhone, CompanySmartPhone, CustomerSmartPhone

class SmartPhoneMain:

    prompt = '''
    주소관리 메뉴
    ------------------
    1. 연락처 등록(회사)
    2. 연락처 등록(거래처)
    3. 모든 연락처 출력
    4. 연락처 검색
    5. 연락처 삭제
    6. 연락처 수정
    7. 엑셀파일 업로드
    8. 프로그램 종료
    ------------------ '''

    def __init__(self):
        self.sp = SmartPhone()

    def start(self):
        while True:
            print(SmartPhoneMain.prompt)
            printMenu = input("원하는 작업을 선택하세요: ")

            if printMenu == '1':
                input_tool = CompanySmartPhone()
                new_data = input_tool.input_addr_data()
                self.sp.add_addr(new_data)

            elif printMenu == '2':
                input_tool = CustomerSmartPhone()
                new_data = input_tool.input_addr_data()
                self.sp.add_addr(new_data)

            elif printMenu == '3':
                self.sp.print_all_addr()

            elif printMenu == '4':
                name = input("검색할 이름을 입력하세요: ")
                self.sp.search_addr(name)

            elif printMenu == '5':
                name = input("삭제할 이름을 입력하세요: ")
                self.sp.delete_addr(name)       
                
            elif printMenu == '6':
                name = input("수정할 연락처의 이름을 입력하세요: ")
                self.sp.edit_addr(name)

            elif printMenu == '7':
                path = input("엑셀 파일 경로를 입력하세요.(xlsx): ")
                self.sp.input_from_excel(path)

            elif printMenu == '8':
                self.sp.save_data()
                print("연락처를 저장하고 프로그램을 종료합니다.")
                break
            else:
                print("메뉴 중에 선택하여 입력해주세요.")




if __name__ == "__main__":
    main_app = SmartPhoneMain()
    main_app.start()