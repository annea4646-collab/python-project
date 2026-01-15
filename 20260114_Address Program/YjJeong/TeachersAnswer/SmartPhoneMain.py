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

class SmartPhoneMain:
    def __init__(self):
        self.smartphone = SmartPhone()  # SmartPhone 인스턴스 생성: 등록, 출력 삭제 등의 명령 대기 상태
                                        # self.smartphone에 저장함으로서 start 메소드 어디서든 꺼내쓸 수 있는 상태
    def print_menu(self):
        print("\n주소관리 메뉴")
        print("-"*15)
        print("1. 연락처 등록")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 프로그램 종료")
        print("-"*15)

    def start(self):
        while True:
            self.print_menu()
            choice =(input("원하는 작업을 선택하세요(1-6): "))

            if choice == '1':
                addr = self.smartphone.input_addr_data()        # 데이터 생성
                self.smartphone.add_addr(addr)                  # 리스트에 추가

            elif choice == '2':
                self.smartphone.print_all_addr()

            elif choice == '3':
                name = input("검색할 이름을 입력하세요: ")
                self.smartphone.search_addr(name)

            elif choice == '4':
                name = input("삭제할 이름을 입력하세요: ")
                self.smartphone.delete_addr(name)       
                
            elif choice == '5':
                name = input("수정할 이름을 입력하세요: ")
                print("새로운 정보를 입력하세요.")
                new_addr = self.smartphone.input_addr_data()
                self.smartphone.edit_addr(name, new_addr)

            elif choice == '6':
                print("프로그램을 종료합니다.")
                break

            else:
                print("숫자 1 ~ 6 중에 선택하여 입력해주세요.")

# 프로그램을 실제로 실행하는 부분
if __name__ == "__main__":                  # 실행의 시작점: 이 파일을 다른 곳에서 import했을 때 메뉴가 갑자기 나오는걸 막아줌
    smartphone_main = SmartPhoneMain()      # SmartPhoneMain 클래스의 __init__ 함수가 자동으로 실행
    smartphone_main.start()                 # 스위치 ON: start() 메서드 안의 while True 무한 루프가 시작


'''
    검문: __main__ 인지 확인 (직접 실행인가?)
    생성: SmartPhoneMain 객체 탄생 (내부적으로 SmartPhone 엔진과 데이터 로딩 완료)
    가동: start() 호출로 무한 루프 진입 (메뉴 출력 및 입력 대기)
'''