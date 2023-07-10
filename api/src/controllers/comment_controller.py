from sqlalchemy.orm import Session
from ..schemas.comment_schema import Comment, CommentCreate, CommentPatch
from ..utils.controller_utils import patch_entity



def comment_get(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def comment_get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Comment).offset(skip).limit(limit).all()

def comment_create(db: Session, comment: CommentCreate):
    db_comment = Comment(
        content=comment.content,
        post_id=comment.post_id,
        comment_id=comment.comment_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def comment_delete(db: Session, comment: Comment):
    db.query(Comment).filter(Comment.id == comment.id).delete(synchronize_session="fetch")

def comment_patch(db: Session, comment: Comment, body: CommentPatch):
    patch_entity(comment, body)
    db.commit()
    db.refresh(comment)
    return comment