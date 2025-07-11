from flask import Flask, request, Response

# import test
# test.py를 실행하면 __name__이 __main__으로 뜨는데 Import로 가져오면 test로 보임

app = Flask(__name__)   # 서버 구축

@app.route('/') # 기본 경로 라우팅 설정
def home() :
    return "Hello, This is Main Page!"

@app.route('/about')    # about page
def about() :
    return "This is the about page!"

@app.route('/company')  
def company() :
    return "This is the company page!"

# 동적으로 URL 파라미터 값을 받아서 처리
@app.route('/user/<username>')
def user_profile(username) :
    return f'UserName : {username}'

@app.route('/number/<int:number>')  # 숫자로 입력받고 싶으면 int: 로 데이터형을 명시해줘야 함 => 문자 입력하면 Not Found
def user_number(number) :
    return f'Number : {number}'

# POST 요청 날리는 법
# (1) postman 프로그램 사용
# (2) requests 모델 사용 - 이거 해볼거임

import requests
@app.route('/test')
def test() :
    url = 'https://127.0.0.1:5000'
    data = 'test_data'
    requests.post(url)  # post 방식으로 요청
    # 뭔가 잘 안됨... Internal Server Error

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELTE'])
def submit() :
    print(request.method)

    if request.method == 'GET' :
        print("GET method")

    if request.method == 'POST' :
        print("***POST method***", request.date)

    return Response('successfully submitted', status=200)

if __name__ == '__main__' :
    # print("__name__ : ", __name__)
    app.run()