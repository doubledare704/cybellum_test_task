__all__ = (
    "posts_bp"
)

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from services.comments import CommentService
from services.posts import PostService

posts_bp = Blueprint('posts', __name__)


@posts_bp.route("/posts", methods=["GET"])
def get_all_posts():
    post_service = PostService()
    posts = post_service.get_all_posts()
    return jsonify([post.to_dict() for post in posts])


@posts_bp.route("/posts/<int:post_id>", methods=["GET"])
def get_post_by_id(post_id):
    post_service = PostService()
    post = post_service.get_post(post_id)

    if post is None:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post.to_dict())


@posts_bp.route("/posts", methods=["POST"])
@jwt_required()
def create_post():
    post_service = PostService()
    data = request.get_json()

    post = post_service.create_post(data)

    return jsonify({
        "message": "User created successfully",
        "post": post.to_dict()
    }), 201


@posts_bp.route("/posts-comments/<int:post_id>", methods=["GET"])
def get_comments_to_post(post_id):
    post_service = PostService()
    post = post_service.get_post(post_id)

    if post is None:
        return jsonify({"error": "Post not found"}), 404

    service = CommentService()
    comments = service.get_comments_to_post(post_id)

    return jsonify([c.to_dict() for c in comments])
