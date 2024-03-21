from sqlalchemy import or_

from models import User, db


class UserRepository:
    def __init__(self):
        self.model = User

    def check_existing_user(self, username: str, email: str) -> User:
        return self.model.query.filter(
            or_(self.model.username == username, self.model.email == email)
        ).first()

    def create_user(self, username, email, hashed_password) -> User:
        user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_username(self, username: str) -> User:
        return self.model.query.filter_by(username=username).first()

    def get_user_by_id(self, user_id: int) -> User:
        return self.model.query.get(user_id)
