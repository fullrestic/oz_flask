from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.user import user_bp
from jwt_utils import configure_jwt

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')

configure_jwt(app)

@app.route('/')
def index() :
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)