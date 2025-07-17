from flask import Flask, render_template, session, make_response, request
from routes.user import user_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.url_map.strict_slashes = False 

# Blueprint 등록
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

app.secret_key = 'pw123'

@app.route("/") 
def index() :
    return "Welcome to the Flask App!"

@app.route('/login')
def login() :
    session['username'] = 'jh'
    return '로그인 완료 -> 세션에 사용자 이름 저장됨'

@app.route('/status')
def status() :
    username = session.get('username')  # 값이 없으면 None 반환
    return f"현재 로그인된 사용자 : {username}"

@app.route('/logout')
def logout() :
    session.pop('username', None)   # pop할 게 없으면 에러 뜨는 것 방지, 없으면 None 배출
    return "로그아웃 완료 -> 세션 만료(제거)"

@app.route('/check')
def check() :
    if 'username' in session :
        return f"{session['username']}님이 현재 로그인 중입니다."
    return f"로그인을 해주세요."

@app.route('/visit')
def visit() :
    if 'visit' not in session :
        session['visit'] = 0
    session['visit'] += 1
    session.modified = True # 임의로 또는 강제로 세션에 반영
    return f'총 {session['visit']}회 방문하셨습니다.'

@app.route('/set')
def set_cookie() :
    resp = make_response('쿠키 설정 완료')
    resp.set_cookie('username', 'kim')
    return resp

@app.route('/get')
def get_cookie() :
    username = request.cookies.get('username')
    return f"저장된 쿠키 : {username}"

if __name__ == "__main__" :
    app.run(debug=True)
