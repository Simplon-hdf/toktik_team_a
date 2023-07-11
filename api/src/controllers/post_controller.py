from sqlalchemy.orm import Session
from ..schemas.post_schema import Post, PostCreate, PostPatch
from ..utils.controller_utils import patch_entity

class PostController:

    @staticmethod
    def get(db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Post).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, post: PostCreate):
        db_post = Post(
            title=post.title,
            description=post.description,
            video_url=post.video_url,
            user_id=post.user_id,
        )
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def delete(db: Session, post: Post):
        db.query(Post).filter(Post.id == post.id).delete(synchronize_session="fetch")

    @staticmethod
    def patch(db: Session, post: Post, body: PostPatch):
        patch_entity(post, body)
        db.commit()
        db.refresh(post)
        return post
