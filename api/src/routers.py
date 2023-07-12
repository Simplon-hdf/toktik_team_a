from fastapi import APIRouter, Depends, HTTPException, Request, Body
from sqlalchemy.orm import Session

from .dto import UserBase, PostCreate, PostPatch, CommentCreate, CommentPatch
from .controllers import UserController, PostController, CommentController
from .dto import User, Post, Comment
from .config import get_db




class UserRouter:

    router = APIRouter(prefix="/user", tags=["user"])

    # Get all
    @router.get("/list", response_model=list[User])
    def post_user(db : Session = Depends(get_db)):
        users = UserController.get_all(db)
        return users

    # Get by token
    @router.get("/token", response_model=None)
    async def post_read(body = Body(...), db: Session = Depends(get_db)):
        user = UserController.get_user_by_token(db, body["token"])
        if user is None:
            raise HTTPException(status_code=404, detail="User is not found")
        return user
    
    # Register
    @router.post("/create", response_model=User)
    def register(user = UserBase, db: Session = Depends(get_db)):
        return UserController.register(db=db, user=user)




class PostRouter:

    router = APIRouter(prefix="/post", tags=["post"])

    @router.post("/create", response_model=Post)
    def post_create(post: PostCreate, db: Session = Depends(get_db)):
        return PostController.create(db=db, post=post)

    @router.get("/list", response_model=list[Post])
    def post_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        posts = PostController.get_all(db, skip=skip, limit=limit)
        return posts

    @router.get("/{post_id}", response_model=Post)
    def post_read(post_id: int, db: Session = Depends(get_db)):
        post = PostController.get(db, post_id=post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    @router.delete("/{post_id}")
    def post_delete(post_id: int, db: Session = Depends(get_db)):
        post = PostController.get(db, post_id=post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return PostController.delete(db=db, post=post)

    @router.patch("/{post_id}", response_model=Post)
    def post_patch(post_id: int, body: PostPatch, db: Session = Depends(get_db)):
        post = PostController.get(db, post_id=post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return PostController.patch(db=db, post=post, body=body)



class CommentRouter:

    router = APIRouter(prefix="/comment", tags=["comment"])

    @router.post("/create", response_model=Comment)
    def comment_create(comment: CommentCreate, db: Session = Depends(get_db)):
        return CommentController.create(db=db, comment=comment)

    @router.get("/list", response_model=list[Comment])
    def comment_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        comments = CommentController.get_all(db, skip=skip, limit=limit)
        return comments

    @router.get("/{comment_id}", response_model=Comment)
    def comment_read(comment_id: int, db: Session = Depends(get_db)):
        comment = CommentController.get(db, comment_id=comment_id)
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment

    @router.delete("/{comment_id}")
    def comment_delete(comment_id: int, db: Session = Depends(get_db)):
        comment = CommentController.get(db, comment_id=comment_id)
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return CommentController.delete(db=db, comment=comment)

    @router.patch("/{comment_id}", response_model=Comment)
    def comment_patch(comment_id: int, body: CommentPatch, db: Session = Depends(get_db)):
        comment = CommentController.get(db, comment_id=comment_id)
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return CommentController.patch(db=db, comment=comment, body=body)
