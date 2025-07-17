from flask import Flask, render_template, session, make_response, request, redirect, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False 

app.secret_key = 'pw123'

@app.route('/')
def index() :
    cookie_user = request.cookies.get('username')
    # 처음 입장하면 쿠키 정보가 없음 -> None
    # 기존에 왔던 사용자의 쿠키 생존시간이 지나서 만료된 경우 -> None

    if 'username' in session and cookie_user is None :
        session.pop('username', None)   # 세션 삭제
        
    # 세션에서 로그인 정보 확인
    username = session.get('username')

    return render_template('index.html', username=username, cookie_user=cookie_user)

@app.route('/login', methods=['GET', 'POST'])
def login() :
    if request.method == 'POST' :
        username = request.form['username']
        
        # 세션과 쿠키에 사용자 이름 저장
        session['username'] = username
        resp = make_response(redirect(url_for('index')))    # 홈화면으로 강제 이동
        resp.set_cookie('username', username, max_age=10)
        return resp
    return render_template('login.html')

@app.route('/logout')
def logtout() :
    session.pop('username', None)
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', max_age=0)
    return resp

if __name__ == "__main__" :
    app.run(debug=True)
