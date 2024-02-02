from flask import Blueprint, jsonify, request
from app.models.user_s_model import Users_s

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = Users_s.query.all()
    user_list = []
    for user in users:
        user_list.append({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'users': user_list})