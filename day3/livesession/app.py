from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/") 
def index() :
    return "Hello, OZ" 

@app.route("/hello/<name>", methods=['GET'], endpoint="hello-oz")
def hello(name : str) -> str :
    return f"Hello, {name}"

@app.route('/hello/<string:username>')  # 숫자 형태로 넣어도 알아서 문자 형태로 바꿔서 타입 에러 뜨지 않음 int로 하고 문자열 넣으면 에러
def hello(username : str) -> str :
    return f"Hello, {username}"

@app.route('/calc/<int:a>/<operator>/<int:b>')
def calculator(a:int, operator:str, b:int)->str :
    try :
        if operator == "add" :
            sum = a + b
            return f"{a} + {b} = {sum}"
        elif operator == "sub" :
            diff = a - b
            return f"{a} - {b} = {diff}"
        elif operator == "mul" :
            mul = a * b
            return f"{a} x {b} = {mul}"
        elif operator == "div" :
            div = a / b
            return f"{a} ÷ {b} = {div}" # 0을 나누거나 3을 0으로 나누는 행위는 파이썬에서 에러로 처리함
        else : 
            return "해당 서비스는 sum(+), sub(-), mul(x), div(÷)만 지원합니다.<br>4가지 중 하나를 입력해주세요."
    except ZeroDivisionError as e :
        return '숫자를 0으로 나눌 수 없습니다.<br>0이 아닌 다른 숫자를 입력해주세요.'


if __name__ == "__main__" :
    app.run(debug=True)

with app.test_request_context() :
    print(url_for('hello-oz', name='jh'))  # 엔드포인트 rule을 이용해 주소 체계를 만들어줌 -> host:0.0.0.123/hello/주현 링크
