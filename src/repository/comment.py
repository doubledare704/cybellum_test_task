from models import User, db, Comment


class CommentRepository:
    def __init__(self):
        self.model = Comment

    def get_all_by_post_id(self, post_id: int) -> list[Comment]:
        return self.model.query.filter(
            self.model.post_id == post_id
        ).all()

    def create_comment(self, data: dict) -> User:
        comment = self.model(**data)
        db.session.add(comment)
        db.session.commit()
        return comment
