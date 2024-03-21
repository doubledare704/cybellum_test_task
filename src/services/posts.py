from typing import List

from models import Post
from repository.post import PostRepository


class PostService:
    def __init__(self, repo: PostRepository = PostRepository()):
        self.repo = repo

    def get_all_posts(self) -> List[Post]:
        return self.repo.get_all()

    def get_post(self, post_id) -> Post:
        return self.repo.get_by_id(post_id)

    def create_post(self, post_dict: dict) -> Post:
        return self.repo.create(post_dict)
