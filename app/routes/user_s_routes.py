from flask import Blueprint, jsonify, request
from app.models.user_s_model import Users_s
from factory import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = Users_s.query.all()
    print(users)
    user_list = []
    for user in users:
        user_list.append({'id': user.id, 'name': user.name})
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

@user_bp.route('/users/get_by_name', methods=['POST'])
def get_user_by_name():
    data = request.get_json()
    name = data.get('name')

    # Validate input (add more validation as needed)
    if not name:
        return jsonify({'error': 'Missing username field'}), 400

    # Query the user by name
    user = Users_s.query.filter_by(name=name).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Return user details
    user_details = {'id': user.id, 'name': user.name}
    return jsonify( user_details)
