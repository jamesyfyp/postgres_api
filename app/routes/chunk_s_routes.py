from flask import Blueprint, jsonify, request
from app.models.chunk_s_model import Chunk_s
from pgvector.sqlalchemy import Vector
from sqlalchemy import select
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

@chunk_bp.route('/chunk/users', methods=['GET'])
def get_unique_user_ids():
    user_ids = db.session.query(Chunk_s.user_id).distinct().all()
    unique_user_ids = [user_id[0] for user_id in user_ids]
    return jsonify({'user_ids': unique_user_ids}), 200

@chunk_bp.route('/chunk/<int:user_id>/posts', methods=['GET'])
def get_unique_posts_for_user(user_id):
    posts = Chunk_s.query.filter_by(user_id=user_id).distinct(Chunk_s.post_id).all()
    unique_post_ids = [post.post_id for post in posts]
    return jsonify({'user_id': user_id, 'unique_post_ids': unique_post_ids}), 200

@chunk_bp.route('/chunk/nearest_neighbors', methods=['POST'])
def get_nearest_neighbors():
     # Get the embedded prompt from the request JSON
    embedded_prompt = request.json.get('embedded_prompt')
    user_id = request.json.get('user_id')
    limit = request.json.get('limit')

    if not embedded_prompt or not user_id:
        return jsonify({'error': 'Missing required fields'}), 400
   
    query = db.session.scalars(select(Chunk_s).filter(Chunk_s.user_id == user_id).order_by(Chunk_s.vector.l2_distance(embedded_prompt)).limit(limit))
    result = query.all()
    results = list(result)
    chunks_list = []
    for row in results:
        chunk_dict = {
            'id': row.id,
            'user_id': row.user_id,
            'post_id': row.post_id,
            'chunk_number': row.chunk_number,
            'text_chunk': row.text_chunk,
            # Add other attributes as needed
        }
        chunks_list.append(chunk_dict)
    return jsonify({"chunks": chunks_list}), 200
