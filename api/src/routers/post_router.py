from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.post_schema import Post, PostCreate, PostPatch
from ..controllers.post_controller import PostController
from ...config import get_db
from ...main import app



@app.post("/create", response_model=Post)
def post_create(tag: PostCreate, db: Session = Depends(get_db)):
    return PostController.post_create(db=db, tag=tag)

@app.get("/list", response_model=list[Post])
def post_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = PostController.get_all(db, skip=skip, limit=limit)
    return posts

@app.get("/{post_id}", response_model=Post)
def post_read(post_id: int, db: Session = Depends(get_db)):
    post = PostController.get(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.delete("/{post_id}")
def post_delete(post_id: int, db: Session = Depends(get_db)):
    post = PostController.get(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostController.delete(db=db, post=post)

@app.patch("/{post_id}", response_model=Post)
def post_patch(post_id: int, body: PostPatch, db: Session = Depends(get_db)):
    post = PostController.get(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostController.patch(db=db, post=post, body=body)
