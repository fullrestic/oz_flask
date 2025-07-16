from flask import Flask, request, url_for, jsonify, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False 

@app.route("/") 
def index() :
    return render_template('index.html', username = '주현')

@app.route("/user")
def get_user() :
    user = {'name' : '주현',
            'age' : 20,
            'skills' : ['Python', 'Flask']}
    return jsonify(user)    # 3.0.0 버전 이상에서 return dict의 경우 자동으로 json화되어서 전송됨

@app.route("/status")
def status_example() :
    data = {'message':'요청이 성공적으로 처리되었습니다.'}
    return jsonify(data), 200

@app.route("/error")
def error_example() :
    error = {'error':'잘못된 요청입니다.'}
    return jsonify(error), 400

@app.route("/custom-header")
def custom_header() :
    response = jsonify({'message':'헤더가 포함된 응답입니다.'})
    response.headers['X-App-Version'] = '1.0.0'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/fruits')
def fruits() :
    fruit_list = ['사과', '바나나', '딸기']
    return render_template('fruits.html', fruits=fruit_list)

@app.route('/check/<int:age>')
def check_age(age) :
    return render_template('age_check.html', age = age)

if __name__ == "__main__" :
    app.run(debug=True)
