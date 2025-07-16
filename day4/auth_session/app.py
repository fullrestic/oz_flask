from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'flask-secret-key' # 실제로 배포시에는 .env or yaml 파일에 저장해서 배포해야함
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)    # 세션 유지 기간 설정

# admin user
users = {
    'john' : 'pw123',
    'leo' : 'pw123'
}

@app.route('/')
def index() :
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login() :   # 폼으로 데이터 받음
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password :
        session['username'] = username  # 세션 생성
        session.permanent = True        # 세션 유지 기간 활성화

        return redirect('/secret')
    else :
        flash("Invalid username or password")
        return redirect('/')

@app.route('/secret')
def secret() :
    if 'username' in session :
        return render_template('secret.html')   # 세션 정보 존재하면 시크릿 페이지 보여줌
    else : 
        return redirect('/')
    
# 로그아웃
@app.route('/logout')
def logout() :
    session.pop('username', None)   # username 제거
    session.clear()
    return redirect('/')

if __name__ == "__main__" :
    app.run(debug=True)