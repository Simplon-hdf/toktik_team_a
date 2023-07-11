from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..schemas.user_schemas import UserSchema, UserCreate
from ..controllers.user_controller import UserController
from ...config import get_db
# from ...main import app

router = APIRouter()

# Get all
@router.get("/list", schema=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    posts = UserController.get_all(db)
    return posts

# Get one by token
@router.get("/", schema = UserSchema)
def get_user_by_token(user: UserSchema, db: Session = Depends(get_db)):
    post = UserController.get_user_by_token(db, token = user.token)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Create user (register)
@router.post( "/create", schema = UserSchema )
def register(db: Session = Depends(get_db), formatedUser = UserCreate):
    return UserController.register(db = db, user = formatedUser)

# Update user
@router.patch("/update", schema = UserSchema)
def update_user(user: UserSchema, db: Session = Depends(get_db)):
    post = UserController.update_user(db, token = user.token)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return UserController.patch(db = db, token = user.token)

# Delete user
@router.delete("/delete", schema = UserSchema)
def delete_user(user: UserSchema, db: Session = Depends(get_db)):
    post = UserController.delete_user(db, token = user.token)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return UserController.delete(db = db, token = user.token)

