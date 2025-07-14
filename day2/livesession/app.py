from flask import Flask, request    # Flask 안에 있는 request 기능 사용

app = Flask(__name__)

@app.route("/") # 기본 주소 main -> 기본 주소 없이 실행하면 에러 발생
def index() :
    return "Hello, OZ"  # Hello, OZ라는 텍스트를 반환해주는 index 함수를 만들었고 기본 URI에 매칭한 상태

@app.route("/search")
def search() :
    keyword = request.args.get('query') # 키가 query인 값을 keyword에 담음
    return f"검색어 : {keyword}"
    # ?query=커피 => 검색어 : 커피

@app.route("/tags")
def tags() :
    keywords = request.args.getlist('tag') # 여러개 값을 한번에 리스트 형태로 가져옴
    return f"태그 목록 : {keywords}"    
    # ?tag=br&tag=div&tag=python => 태그 목록 : ['br', 'div', 'python']

@app.route("/shop")
def shop() :
    keyword = request.args.get('keyword')
    category = request.args.get('category')
    return f"검색어 : {keyword}<br>카테고리 : {category}"

@app.route("/filter")
def filter() :
    filter = request.args.getlist('filter')
    return f"필터 : {filter}"

@app.route('/user/<username>')  # 변수 받아오기
def show_user_profile(username) :
    return f"안녕하세요, {username}님"

@app.route('/greet/<username>/<int:age>')
def greet(username, age) :
    return f"안녕, {username}! 나는 {age}살이야 우리 친구하자."

if __name__ == "__main__" :
    app.run(debug=True) # 이렇게 추가해주면 flask run 명령어 없이 파일만 실행 시키면 됨
        
