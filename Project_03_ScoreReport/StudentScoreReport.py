import os
import oracledb
from dotenv import load_dotenv
from Student import Student

try:
    oracledb.init_oracle_client() 
except Exception as e:
    pass

load_dotenv()

class StudentScoreReport:
    def __init__(self):
        self.student_list = []

        user = os.getenv("DB_USER")
        pw = os.getenv("DB_PASSWORD")
        dsn = os.getenv("DB_DSN")
        # DB 연결 및 테이블 생성
        try:
            self.conn = oracledb.connect(user=user, password=pw, dsn=dsn)
            self.cursor = self.conn.cursor()
        
            self.cursor.execute('''
                            BEGIN
                                EXECUTE IMMEDIATE 'CREATE TABLE students (
                                    id NUMBER PRIMARY KEY,
                                    name VARCHAR2(50),
                                    kor NUMBER,
                                    eng NUMBER,
                                    math NUMBER,
                                    total NUMBER,
                                    avg NUMBER
                                )';
                            EXCEPTION
                                WHEN OTHERS THEN
                                    IF SQLCODE = -955 THEN NULL; ELSE RAISE; END IF;
                            END;
                        ''')
        except oracledb.Error as e:
            print(f"오라클 연결 실패: {e}")


    def add_to_db(self, s):
        try:
        # 1. 먼저 DB에 몇 명이 있는지 확인
            self.cursor.execute("SELECT COUNT(*) FROM students")
            count = self.cursor.fetchone()[0]

            if count >= 10:
                print(" DB 저장 용량이 가득 찼습니다. (전체 최대 10명)")
                return

            # SQL 쿼리로 데이터 삽입
            sql = """
                INSERT INTO students (id, name, kor, eng, math, total, avg) 
                VALUES (student_seq.NEXTVAL, :1, :2, :3, :4, :5, :6)
            """

            data = (s.name, s.korscore, s.engscore, s.mathscore, s.total_score(), s.avg_score())

            self.cursor.execute(sql, data)
            self.conn.commit()
            print(f"---{s.name} 데이터 Oracle 저장 완료")
        except oracledb.Error as e:
            print(f"데이터 오류: {e}")
            
    def close_db(self):
         if hasattr(self, 'conn'):
            self.conn.close()


    def input_data(self):
            print("성적 입력 >>>")
            name = input("학생이름: ")
            korscore = input("국어점수: ")
            engscore = input("영어점수: ")
            mathscore = input("수학점수: ")
            return name, korscore, engscore, mathscore
    
    def add_list(self, student_obj):
        if len(self.student_list) >= 10:
            print("저장 공간이 부족합니다. (최대 10개)")
            return
        self.student_list.append(student_obj)
        print(f">>> {student_obj.name} 저장 완료")


report = StudentScoreReport()

if __name__ == "__main__":
    while True:
        name, korscore, engscore, mathscore = report.input_data()
        new_student = Student(name, korscore, engscore, mathscore)

        report.add_list(new_student)   
        report.add_to_db(new_student)  # SQL DB에 추가

        menu = input("\n 계속 입력하시겠습니까? (y/n): ")
        if menu.lower() != 'y':
            break
     
print("### Score Report ###")
print("국어\t영어\t수학\t|\t총합\t평균")
print("-"*50)

for s in report.student_list:
     print(f"{s.korscore}\t{s.engscore}\t{s.mathscore}\t|\t{s.total_score()}\t{s.avg_score():.0f}")

report.close_db()




