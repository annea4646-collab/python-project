
''' 연락처 정보를 관리하는 클래스
     - Addr 클래스의 인스턴스 10개를 저장할 수 있는 리스트 정의
     - 리스트에 인스턴스 저장하고, 수정, 삭제, 저장된 데이터의 리스트를 출력하는 메소드 정의
'''
# pip install pandas openpyxl
import pickle                       # 데이터 저장
import pandas as pd                 # 엑셀 파일 등록

from Address import Addr

class SmartPhone:

    def __init__(self):
        self.list = []

    def input_addr_data(self):        # 키보드로부터 입력 받아 객체를 생성함
        # 데이터 수집
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        group = input("그룹(친구/가족)을 입력하세요: ")
        
        # 객체 생성
        addr_obj = Addr(name, phone, email, address, group)        

        # 결과물 반환
        return addr_obj

    def add_addr(self, addr_obj):              # 연락처 객체 저장
        # 현재 리스트에 10명 이상 있다면 저장공간 부족
        if len(self.list) >= 10:
            print(f"저장공간이 부족하여 {addr_obj.name}님을 추가할 수 없습니다.")
            return
        
        self.list.append(addr_obj)
        print(f">>> {addr_obj.name} 데이터가 저장되었습니다.")

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




    def input_from_excel(self, file_path):
        try:
            # 엑셀파일 읽기(첫째 행은 Header: name, phone, email, address, group)
            # 첫 행이 제목이 아니라고 알려주는 옵션 read_excel(file_path, header=None)
            df = pd.read_excel(file_path)

            # 액셀 각 행(row) 돌며 객체 생성
            for _, row in df.iterrows():    # data행(2행)부터 반복 시작, 필요없는 값은 _라는 변수에 담아버린다
                # 각 열의 데이터 가져와 Addr 객체 생성
                new_addr = Addr(
                    name = str(row['name']),
                    phone= str(row['phone']),
                    email= str(row['email']),
                    address= str(row['address']),
                    group= str(row['group'])
                )

                self.addAddr(new_addr)

            print(f"엑셀파일 {file_path}로부터 {len(df)}개의 연락처를 불러왔습니다.")
        except Exception as e:
            print(f"엑셀 로드 중 오류 발생: {e}")


    def print_group_addr(self, target_group):
        # 전체 리스트에서 그룹이 일치하는 값만 모아서 새로운 리스트 생성
        filtered_list = [contact for contact in self.list if contact.group == target_group]

        # 결과 출력
        if not filtered_list:
            print(f"{target_group} 그룹에 등록된 연락처가 없습니다.")
        else:
            print(f"{target_group} 그룹 검색 결과 ({len(filtered_list)}명)")
            for i, contact in enumerate(filtered_list, start=1):        # 원본 list의 index와 상관없이 순차적으로 결과 보여줌
                print(f"[{i}]")
                contact.print_info()

    def save_data(self):
        # addr_data.pkl 이름의 이진 파일(wb)로 리스트를 통째로 저장
        with open("addr_data.pkl", "wb") as f:
            pickle.dump(self.list, f)
        print("모든 데이터가 파일(addr_data.pkl)에 안전하게 저장되었습니다.")

    def load_data(self):
        import os
        # 파일 존재 여부 확인
        if os.path.exists("addr_data.pkl"):
            with open("addr_data.pkl", "rb") as f:
                self.list = pickle.load(f)
            print(f"이전에 저장된 {len(self.list)}개의 연락처를 불러왔습니다.")
        else:
            print("저장된 데이터 파일이 없어 새로 시작합니다.")