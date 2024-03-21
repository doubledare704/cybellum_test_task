from flask_jwt_extended import create_access_token

from repository.user import UserRepository


class UserService:

    def __init__(self, repo: UserRepository = UserRepository()):
        self.repo = repo

    def check_existing(self, username: str, email: str):
        return self.repo.check_existing_user(username, email)

    def create_user(self, username, email, hashed_password):
        return self.repo.create_user(username, email, hashed_password)

    def get_user_by_username(self, username: str):
        return self.repo.get_user_by_username(username)

    def get_user_by_id(self, user_id: int):
        return self.repo.get_user_by_id(user_id)

    def new_access_token(self, user):
        return create_access_token(identity=user.id)
