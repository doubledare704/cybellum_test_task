import os
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from models import db
from utils import temp_blocked_jwts
from views import comments_bp, posts_bp, users_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://user:password@localhost:5432/blog_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.config["JWT_SECRET_KEY"] = "ee9e330571a595a3412feb657db4d117cd42d0d8"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]

    return jti in temp_blocked_jwts


app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(comments_bp)
