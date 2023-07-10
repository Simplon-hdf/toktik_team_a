from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.comment_schema import Comment, CommentCreate, CommentPatch
from ..controllers.comment_controller import CommentController
from ...config import get_db
from ...main import app

@app.post("/create", response_model=Comment)
def comment_create(tag: CommentCreate, db: Session = Depends(get_db)):
    return CommentController.comment_create(db=db, tag=tag)

@app.get("/list", response_model=list[Comment])
def comment_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = CommentController.get_all(db, skip=skip, limit=limit)
    return comments

@app.get("/{comment_id}", response_model=Comment)
def comment_read(comment_id: int, db: Session = Depends(get_db)):
    comment = CommentController.get(db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@app.delete("/{comment_id}")
def comment_delete(comment_id: int, db: Session = Depends(get_db)):
    comment = CommentController.get(db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return CommentController.delete(db=db, comment=comment)

@app.patch("/{comment_id}", response_model=Comment)
def comment_patch(comment_id: int, body: CommentPatch, db: Session = Depends(get_db)):
    comment = CommentController.get(db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return CommentController.patch(db=db, comment=comment, body=body)
