from flask import Blueprint, jsonify, request 
from app.models.user_s_model import Users_s
from app.models.post_s_model import Post_s
from factory import db

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['GET'])
def get_all_posts():
    posts = Post_s.query.all()
    post_list = "hi"
    # for post in posts:
    #     post_list.append({'id': post.id, 'title': post.title, 'content': post.content})
    return jsonify(post_list)

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()

    user_id = data.get('user_id')
    title = data.get("title")
    content = data.get('content')

    if not (user_id and title and content): 
        return jsonify({'error': 'Missing required fields'}), 400
    
    
    
    new_post = Post_s( title=title, user_id= user_id, content=content)

    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully', 'post_id': new_post.id}), 201