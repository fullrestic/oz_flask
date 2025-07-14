from flask import request
from flask_smorest import Blueprint, abort

def create_user_blueprint(mysql) :
    user_blp = Blueprint("user_routes", __name__, url_prefix='/users')

    # 전체 유저 데이터를 불러오는 함수
    @user_blp.route('/', methods=['GET'])
    def get_users() :
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()   # return 타입은 튜플
        cursor.close()

        # REST API => {}
        # 딕셔너리 형태로 변환 필요
        users_list = []
        for user in users :
            users_list.append({
                'id' : user[0],
                'name' : user[1],
                'email' : user[2]
            })

        return users_list
    

    # 유저 생성 함수
    @user_blp.route("/", methods=['POST'])
    def add_user() :
        user_data = request.json

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s)",
                       (user_data['name'], user_data['email']))
        mysql.connection.commit()   # 쿼리문 실행
        cursor.close()
        
        return {'msg':'successfully added user'}, 201
    

    # 유저를 업데이트하는 함수 (UPDATE)
    @user_blp.route('/<int:user_id>', methods=['PUT'])
    def update_user(user_id) :
        user_data = request.json

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s",
                       (user_data['name'], user_data['email'], user_id))
        
        mysql.connection.commit()
        cursor.close()

        return {'msg':'successfully updated user'}, 201


    # 유저를 삭제하는 함수 (DELETE)
    @user_blp.route('/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id) :
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cursor.close()

        return {'msg':'successfully deleted user'}, 201

    return user_blp