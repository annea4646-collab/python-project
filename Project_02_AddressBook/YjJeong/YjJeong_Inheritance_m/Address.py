from dataclasses import dataclass

@dataclass
class Addr:
    name: str; 
    phone: str; 
    email: str; 
    address: str; 
    birth: str; 
    role: str

    def print_info(self):
        print(f"이름: {self.name}")
        print(f"전화번호: {self.phone}")
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}")
        print(f"생일: {self.birth}")
        print(f"직급: {self.role}")

    def update_info(self):
        def get_input(label, current):
            val = input(f"{label} (현재: {current}): ")
            return val if val else current

        self.name = get_input("이름", self.name)
        self.phone = get_input("전화번호", self.phone)
        self.email = get_input("이메일", self.email)
        self.address = get_input("주소", self.address)
        self.birth = get_input("생일", self.birth)
        self.role = get_input("직급", self.role)

@dataclass
class CompanyAddr(Addr):
    company: str; 
    dept: str

    def print_info(self):
        super().print_info()
        print(f"회사: {self.company}")
        print(f"부서: {self.dept}")

    def update_info(self):
        super().update_info() 
        val = input(f"회사 (현재: {self.company}): ")
        if val: self.company = val
        val = input(f"부서 (현재: {self.dept}): ")
        if val: self.dept = val

@dataclass
class CustomerAddr(Addr):
    client: str; 
    item: str

    def print_info(self):
        super().print_info()
        print(f"거래처: {self.client}")
        print(f"품목: {self.item}")

    def update_info(self):
        super().update_info()
        val = input(f"거래처 (현재: {self.client}): ")
        if val: self.client = val
        val = input(f"품목 (현재: {self.item}): ")
        if val: self.item = val