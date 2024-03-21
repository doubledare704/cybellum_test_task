__all__ = (
    "comments_bp"
)

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.comments import CommentService

comments_bp = Blueprint('comments', __name__)


@comments_bp.route("/comments", methods=["POST"])
@jwt_required()
def create_comment():
    identity = get_jwt_identity()
    service = CommentService()
    data = request.get_json()
    data["author_id"] = identity
    comment = service.create_comment(data)

    return jsonify({
        "message": "Comment created successfully",
        "post": comment.to_dict()
    }), 201
