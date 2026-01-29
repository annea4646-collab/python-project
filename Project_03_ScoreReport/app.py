from flask import Flask, render_template, request, redirect
from Student import Student
from StudentScoreReport import StudentScoreReport  # 기존 파일명으로 임포트

app = Flask(__name__)
report = StudentScoreReport()

@app.route('/')
def index():
    # DB에서 현재 리스트를 가져와 화면에 보여줌
    return render_template('index.html', students=report.student_list)

@app.route('/add', methods=['POST'])
def add_student():
    # HTML 폼에서 입력한 데이터 받기
    name = request.form['name']
    kor = request.form['kor']
    eng = request.form['eng']
    math = request.form['math']
    
    # 객체 생성 및 리스트/DB 추가
    new_student = Student(name, kor, eng, math)
    report.add_list(new_student)
    report.add_to_db(new_student)
    
    return redirect('/') # 다시 메인 페이지로

if __name__ == '__main__':
    app.run(debug=True)