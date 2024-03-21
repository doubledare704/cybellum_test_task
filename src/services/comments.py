from models import Comment
from repository.comment import CommentRepository


class CommentService:
    def __init__(self, repo: CommentRepository = CommentRepository()):
        self.repo = repo

    def create_comment(self, data: dict) -> Comment:
        return self.repo.create_comment(data)

    def get_comments_to_post(self, post_id: int) -> list[Comment]:
        return self.repo.get_all_by_post_id(post_id)
