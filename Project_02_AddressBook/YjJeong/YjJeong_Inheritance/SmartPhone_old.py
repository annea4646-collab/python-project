
''' 연락처 정보를 관리하는 클래스
     - Addr 클래스의 인스턴스 10개를 저장할 수 있는 리스트 정의
     - 리스트에 인스턴스 저장하고, 수정, 삭제, 저장된 데이터의 리스트를 출력하는 메소드 정의
'''


from Address import Addr, CompanyAddr, CustomerAddr


class SmartPhone:

    def __init__(self):
        self.list = []

    def input_addr_data(self):        # 키보드로부터 입력 받아 객체를 생성함
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        birth = input("생일을 입력하세요: ")
        role = input("직급을 입력하세요: ")
        
        # addr_obj = Addr(name, phone, email, address, birth, role)        
        return name, phone, email, address, birth, role


    def add_addr(self, addr_obj):              # 연락처 객체 저장    
        self.list.append(addr_obj)
        print(f">>> {addr_obj.name}님 정보가 저장되었습니다.")

    def print_addr(self, index):            # 객체 정보 출력
        if 0 <= index < len(self.list):
            self.list[index].print_info()

    def print_all_addr(self):         # 모든 연락처 출력
        if len(self.list) == 0:
            print("저장된 연락처가 없습니다.")
            return

        for i in range(len(self.list)):
            print(f"[{i+1}]")
            self.print_addr(i)

    def search_addr(self, target_name):           # 연락처 검색
        temp_dict = {contact.name: contact for contact in self.list}

        if target_name in temp_dict:
            print(f'--- {target_name}님의 정보 ---')
            temp_dict[target_name].print_info()
        else:
            print(f"{target_name}님을 찾을 수 없습니다.")

    def delete_addr(self, target_name):           # 연락처 삭제
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


    def edit_addr(self, target_name):             # 연락처 수정
        found_contact = None
        for contact in self.list:
            if contact.name == target_name:
                found_contact = contact
                break

        if found_contact:
            print(f"{target_name}님 정보를 수정합니다.")
            print("(수정하지 않으려면 엔터를 치세요!)")

            new_name = input(f"이름 (현재: {found_contact.name}): ")
            if new_name:
                found_contact.name = new_name

            new_phone = input(f"전화번호 (현재: {found_contact.phone}): ")
            if new_phone:
                found_contact.phone = new_phone

            new_email = input(f"이메일 (현재: {found_contact.email}): ")
            if new_email:
                found_contact.email = new_email

            new_address = input(f"주소 (현재: {found_contact.address}): ")
            if new_address:
                found_contact.address = new_address

            new_birth = input(f"생일 (현재: {found_contact.birth}): ")
            if new_birth:
                found_contact.group = new_birth

            new_role = input(f"직급 (현재: {found_contact.role}): ")
            if new_role:
                found_contact.role = new_role

            if isinstance(found_contact, CompanyAddr):
                new_company = input(f"회사 (현재: {found_contact.company}): ")
                if new_company:
                    found_contact.company = new_company
                new_dept = input(f"부서 (현재: {found_contact.dept}): ")
                if new_dept:
                    found_contact.dept = new_dept

            elif isinstance(found_contact, CustomerAddr):
                new_client = input(f"거래처 (현재: {found_contact.client}): ")
                if new_client:
                    found_contact.client = new_client
                new_item = input(f"품목 (현재: {found_contact.item}): ")
                if new_item:
                    found_contact.item = new_item

            print("수정이 완료되었습니다.")

        else:
            print(f"{target_name}님을 찾을 수 없습니다.")


class CompanySmartPhone(SmartPhone): 
    def __init__(self):
        super().__init__()

    def input_addr_data(self):
        name, phone, email, address, birth, role  = super().input_addr_data()
        company = input("회사 이름을 입력하세요: ")
        dept = input("부서 이름을 입력하세요: ")

        return CompanyAddr(name, phone, email, address, birth, role, company, dept)


class CustomerSmartPhone(SmartPhone): 
    def __init__(self):
        super().__init__()
    
    def input_addr_data(self):
        name, phone, email, address, birth, role  = super().input_addr_data()
        client = input("거래처 이름을 입력하세요: ")
        item = input("품목 이름을 입력하세요: ")

        return CustomerAddr(name, phone, email, address, birth, role, client, item)
    

class SafeSmartPhone(SmartPhone):
    def add_addr(self, addr_obj):
        try:
            if len(self.list) >= 10:
                raise ValueError("저장공간이 부족합니다.")
            super().add_addr(addr_obj)
        except ValueError as e:
            print(f"시스템 알림: {e}")



class EditAddrCompanySmartPhone(SmartPhone):
    def edit_addr(self, target_name):             # 연락처 수정
        found_contact = None
        for contact in self.list:
            if contact.name == target_name:
                found_contact = contact
                break

        if found_contact:
            super().edit_addr(target_name)

            new_name = input(f"이름 (현재: {found_contact.name}): ")
            if new_name:
                found_contact.name = new_name

            new_phone = input(f"전화번호 (현재: {found_contact.phone}): ")
            if new_phone:
                found_contact.phone = new_phone

            print("수정이 완료되었습니다.")

        else:
            print(f"{target_name}님을 찾을 수 없습니다.")