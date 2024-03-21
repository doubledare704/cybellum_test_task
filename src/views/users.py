__all__ = (
    "users_bp"
)

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt

from services.users import UserService
from utils import generate_password_hash, hash_is_valid, temp_blocked_jwts

users_bp = Blueprint('users', __name__)


@users_bp.route("/users", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    user_service = UserService()
    existing_user = user_service.check_existing(username, email)
    if existing_user:
        return jsonify({"error": "Username or email already exists"}), 400

    hashed_password = generate_password_hash(password)
    user_service.create_user(username, email, hashed_password)

    return jsonify({
        "message": "User created successfully"
    }), 201


@users_bp.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id: int):
    user_service = UserService()
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Username doesn't exist"}), 404

    return jsonify(user.to_dict()), 201


@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user_service = UserService()

    if not username or not password:
        return jsonify({"error": "Missing required fields"}), 400

    user = user_service.get_user_by_username(username)
    if user is None:
        return jsonify({"error": "Invalid credentials"}), 401

    if not hash_is_valid(password, user.password_hash):
        return jsonify({"error": "Invalid credentials"}), 401

    # Login successful, generate JWT token
    access_token = user_service.new_access_token(user)
    return jsonify({"message": "Login successful", "access_token": access_token})


@users_bp.route("/logout", methods=["POST"])
@jwt_required(verify_type=False)
def logout():
    token = get_jwt()
    jti = token["jti"]
    temp_blocked_jwts.append(jti)
    return jsonify({"message": "Logout finished"})