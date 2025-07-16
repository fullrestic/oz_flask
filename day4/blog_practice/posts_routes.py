from flask import request, jsonify
from flask_smorest import Blueprint, abort

# API CRUD

def create_posts_blueprint(mysql) :
    posts_blp = Blueprint("posts", __name__, description='posts api', url_prefix='/posts')

    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts() :
        cursor = mysql.connection.cursor()
        
        # 게시글 조회
        if request.method == 'GET' :
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts :
                post_list.append({
                    'id' : post[0],
                    'title' : post[1],
                    'content' : post[2]
                })

            return jsonify(post_list)
        
        # 게시글 생성
        elif request.method == 'POST' :
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content :
                abort(400, message="Title or Content cannot be empty")

            sql = 'INSERT INTO posts(title, content) VALUES(%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()
            cursor.close()

            return jsonify({'msg':'Successfully created post data', 'title':title, 'content':content}), 201
        
        cursor.close()
            
    # 특정 게시글 조회
    # 게시글 수정 및 삭제

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id) :
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM posts WHERE id = {id}"
        cursor.execute(sql)
        post = cursor.fetchone()

        if request.method == 'GET' :
            cursor.close()
            if not post :
                abort(404, "Post Not Found")
            return jsonify({
                    'id' : post[0],
                    'title' : post[1],
                    'content' : post[2]
                })
        
        elif request.method == 'PUT' :
            # data = request.json
            # title = data['title']
            # 이런 방식으로 해도 됨
            
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content : 
                abort(400, "Title, Content Not Found")

            if not post : 
                abort(404, "Post Not Found")

            sql = f"UPDATE posts SET title={title}, content={content} WHERE id={id}"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()

            return jsonify({"msg":"Successfully updated title & content"})

        elif request.method == 'DELETE' :
            if not post : 
                abort(404, "Post Not Found")

            sql = f"DELETE FROM posts WHERE id={id}"
            cursor.execute(sql)
            mysql.connection.commit()  
            cursor.close()  

            return jsonify({"msg":"Successfully deleted title & content"}) 

        cursor.close()       
    
    return posts_blp
