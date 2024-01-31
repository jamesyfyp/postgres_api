from flask import Blueprint, jsonify, request
from app.models.post_s_model import Post_s, db

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['GET'])
def get_all_posts():
    # posts = Post.query.all()
    # post_list = []
    # for post in posts:
    #     post_list.append({'id': post.id, 'title': post.title, 'content': post.content})
    return jsonify({'posts': 'ash is cute'})