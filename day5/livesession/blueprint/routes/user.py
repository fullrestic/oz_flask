from flask import Blueprint, render_template

# Blueprint 객체 생성
user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/<username>')
def username(username) :
    return render_template('user.html', username=username)