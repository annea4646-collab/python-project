''' @dataclass는
     1. input : __init))이 없는 껍데기 Addr 클래스
     2. Process : 필드 명세(name:str)를 분석하여 필요한 메서드 __init__를 코딩(작성)해줌
     3. Output : __init__이 장착된 완성형 Addr 클래스
'''

from dataclasses import dataclass

@dataclass
class Addr:
    # 1. 타입 힌트와 함께 필드 선언 ( 자동으로 __init__ 생성됨)
    name: str
    phone: str
    email: str
    address: str
    group: str = "친구"                 #기본값 설정 가능

    # 2. 정보 출력 메서드
    def print_info(self):
        #Getter/Setter 없이 직접 속성에 접근 (Pythonic)
        print(f"이름: {self.name}")
        print(f"전화번호: {self.phone}")
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}")
        print(f"그룹(친구/가족): {self.group}")
