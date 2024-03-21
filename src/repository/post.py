from models import Post, db


class PostRepository:
    def __init__(self):
        self.model = Post

    def get_all(self) -> list[Post]:
        return self.model.query.all()

    def get_by_id(self, post_id: int) -> Post:
        return self.model.query.get(post_id)

    def create(self, post: dict) -> Post:
        post_record = self.model(**post)
        db.session.add(post_record)
        db.session.commit()
        return post_record
