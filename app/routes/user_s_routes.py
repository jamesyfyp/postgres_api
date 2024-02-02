from flask import Blueprint, jsonify, request
from app.models.user_s_model import Users_s
from factory import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = Users_s.query.all()
    user_list = []
    for user in users:
        user_list.append({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'users': user_list})

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    name = data.get('name')

    if not name: 
        return jsonify({'error': 'Missing required fields'}), 400
    
    existing_user = Users_s.query.filter(Users_s.name == name).first()
    
    if existing_user: 
        return jsonify({'error': 'name exists'}), 400
    
    new_user = Users_s(name=name)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201