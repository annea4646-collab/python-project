import os
import pickle
import pandas as pd

from Address import Addr, CompanyAddr, CustomerAddr

class SmartPhone:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "addr_data.pkl")

        self.list = []
        self.load_data()

    def input_common_data(self):
        name = input("이름: "); 
        phone = input("전화번호: "); 
        email = input("이메일: ")
        addr = input("주소: "); 
        birth = input("생일: "); 
        role = input("직급: ")
        return name, phone, email, addr, birth, role

    def add_addr(self, addr_obj):
        if len(self.list) >= 10:
            print(">>> 저장 공간이 부족합니다 (최대 10개).")
            return
        self.list.append(addr_obj)
        print(f">>> {addr_obj.name}님 저장 완료.")

    def find_contact(self, name):
        for contact in self.list:
            if contact.name == name: return contact
        return None

    def edit_addr(self, target_name):
        contact = self.find_contact(target_name)
        if contact:
            print(f"--- {target_name}님 정보 수정 ---")
            # 다형성: contact가 무엇이든 자기 클래스의 update_info를 실행함
            contact.update_info()
            print(">>> 수정이 완료되었습니다.")
        else:
            print(f">>> {target_name}님을 찾을 수 없습니다.")

    def print_all_addr(self):
        if not self.list:
            print("저장된 연락처가 없습니다.")
            return
        for i, contact in enumerate(self.list):
            print(f"[{i+1}]")
            contact.print_info()

    def search_addr(self, target_name):
        """연락처 검색 및 상세 출력"""
        found_contact = self.find_contact(target_name)

        if found_contact:
            print(f"--- {target_name}님의 정보 ---")
            found_contact.print_info()  # 데이터 객체가 가진 출력 기능 활용
        else:
            print(f"{target_name}님을 찾을 수 없습니다.")

    def delete_addr(self, target_name):
        contact = self.find_contact(target_name)
        if contact:
            if input(f"{target_name}님을 삭제할까요? (y/n): ").lower() == 'y':
                self.list.remove(contact)
                print("삭제되었습니다.")
        else:
            print("찾을 수 없습니다.")



# ''' upgrade '''
    def input_from_excel(self, file_path):
        try:
            if not os.path.isabs(file_path):
                file_path = os.path.join(self.base_dir, file_path
                                         )
            # 엑셀 읽기 (헤더: name, phone, email, address, birth, role, type, extra1, extra2)
            df = pd.read_excel(file_path)

            for _, row in df.iterrows():
                # 데이터 타입 확인 (회사/거래처/일반)
                addr_type = str(row.get('type', '일반'))
                
                # 공통 데이터 추출
                args = {
                    'name': str(row['name']),
                    'phone': str(row['phone']),
                    'email': str(row['email']),
                    'address': str(row['address']),
                    'birth': str(row['birth']),
                    'role': str(row['role'])
                }

                # 타입에 따른 객체 생성
                if addr_type == '회사':
                    new_addr = CompanyAddr(**args, company=str(row['extra1']), dept=str(row['extra2']))
                elif addr_type == '거래처':
                    new_addr = CustomerAddr(**args, client=str(row['extra1']), item=str(row['extra2']))
                else:
                    new_addr = Addr(**args)

                self.add_addr(new_addr)

            print(f">>> 엑셀 파일 {file_path}로부터 {len(df)}개의 연락처를 불러왔습니다.")
        except Exception as e:
            print(f">>> 엑셀 로드 중 오류 발생: {e}")


    # --- 데이터 저장 (Pickle 이용) ---
    def save_data(self):
        try:
            with open(self.db_path, "wb") as f:
                pickle.dump(self.list, f)
            print(f">>> 모든 데이터가 저장되었습니다.{self.db_path}")
        except Exception as e:
            print(f">>> 데이터 저장 중 오류 발생: {e}")

    # --- 데이터 불러오기 (Pickle 이용) ---
    def load_data(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, "rb") as f:
                    self.list = pickle.load(f)
                print(f">>> 시스템: 이전에 저장된 {len(self.list)}개의 연락처를 불러왔습니다.")
            except Exception as e:
                print(f">>> 데이터 로드 중 오류 발생: {e}")
                self.list = []
        else:
            print(">>> 시스템: 저장된 데이터 파일이 없어 새로 시작합니다.")
            
# ''' end '''



class CompanySmartPhone(SmartPhone):
    def input_addr_data(self):
        data = self.input_common_data()
        com = input("회사: "); 
        dept = input("부서: ")
        return CompanyAddr(*data, com, dept)

class CustomerSmartPhone(SmartPhone):
    def input_addr_data(self):
        data = self.input_common_data()
        client = input("거래처: "); 
        item = input("품목: ")
        return CustomerAddr(*data, client, item)