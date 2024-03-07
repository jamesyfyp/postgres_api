from flask import Blueprint, jsonify, request
from app.models.chunk_s_model import Chunk_s
from factory import db

chunk_bp = Blueprint('chunk_bp', __name__)

@chunk_bp.route('/chunk', methods=['POST'])
def create_chunk():
    data = request.get_json()

    user_id = data.get('user_id')
    post_id = data.get('post_id')
    chunk_number = data.get('chunk_number')
    text_chunk = data.get('text_chunk')
    vector = data.get('vector')

    if not user_id or not post_id: 
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_chunk = Chunk_s(user_id=user_id, post_id=post_id, chunk_number=chunk_number, text_chunk=text_chunk, vector=vector)

    db.session.add(new_chunk)
    db.session.commit()

    return jsonify({'message': 'Chunk created successfully'}), 201
