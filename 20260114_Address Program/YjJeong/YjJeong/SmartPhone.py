
''' 연락처 정보를 관리하는 클래스
     - Addr 클래스의 인스턴스 10개를 저장할 수 있는 리스트 정의
     - 리스트에 인스턴스 저장하고, 수정, 삭제, 저장된 데이터의 리스트를 출력하는 메소드 정의
'''


from Address import Addr

class SmartPhone:

    def __init__(self):
        self.list = []

    def inputAddrData(self):        # 키보드로부터 입력 받아 객체를 생성함
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        group = input("그룹(친구/가족)을 입력하세요: ")
        
        addr_obj = Addr(name, phone, email, address, group)        
        return addr_obj


    def addAddr(self, addr_obj):              # 연락처 객체 저장
        # 현재 리스트에 10명 이상 있다면 저장공간 부족
        if len(self.list) >= 10:
            print(f"저장공간이 부족하여 {addr_obj.name}님을 추가할 수 없습니다.")
            return
        
        self.list.append(addr_obj)
        print(f">>> {addr_obj.name} 데이터가 저장되었습니다.")

    def printAddr(self, index):            # 객체 정보 출력
        if 0 <= index < len(self.list):
            self.list[index].print_info()

    def printAllAddr(self):         # 모든 연락처 출력
        if len(self.list) == 0:
            print("저장된 연락처가 없습니다.")
            return

        for i in range(len(self.list)):
            print(f"[{i+1}]")
            self.printAddr(i)

    def searchAddr(self, target_name):           # 연락처 검색
        temp_dict = {contact.name: contact for contact in self.list}

        if target_name in temp_dict:
            print(f'--- {target_name}님의 정보 ---')
            temp_dict[target_name].print_info()
        else:
            print(f"{target_name}님을 찾을 수 없습니다.")

    def deleteAddr(self, target_name):           # 연락처 삭제
        found_contact = None

        for contact in self.list:
            if contact.name == target_name:
                found_contact = contact
                break

        if found_contact:
            answer = input(f"{target_name}님을 삭제하시겠습니까? (y/n) ")
            if answer.lower() == 'y':
                self.list.remove(found_contact)
                print(f"{target_name}님 연락처가 삭제되었습니다.")
            else:
                print("삭제가 취소되었습니다.")
        else:
            print(f"{target_name}님을 찾을 수 없습니다.")


    def editAddr(self, target_name):             # 연락처 수정
        found_contact = None
        for contact in self.list:
            if contact.name == target_name:
                found_contact = contact
                break

        if found_contact:
            print(f"{target_name}님 정보를 수정합니다.")
            print("(수정하지 않으려면 엔터를 치세요!)")

            new_name = input(f"새 이름 (현재: {found_contact.name}): ").strip()
            if new_name:
                found_contact.name = new_name

            new_phone = input(f"새 전화번호 (현재: {found_contact.phone}): ").strip()
            if new_phone:
                found_contact.phone = new_phone

            new_email = input(f"새 이메일 (현재: {found_contact.email}): ").strip()
            if new_email:
                found_contact.email = new_email

            new_address = input(f"새 주소 (현재: {found_contact.address}): ").strip()
            if new_address:
                found_contact.address = new_address

            new_group = input(f"새 그룹 (현재: {found_contact.group}): ").strip()
            if new_group:
                found_contact.group = new_group

            print("수정이 완료되었습니다.")

        else:
            print(f"{target_name}님을 찾을 수 없습니다.")



