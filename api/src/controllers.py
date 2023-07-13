from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import datetime, timezone
import re
from jwt import encode
from .config import SECURE_KEY
from datetime import datetime, timezone
import hashlib

from .models import UserSchema, PostSchema, CommentSchema
from .dto import PostCreate, PostPatch, CommentCreate, CommentPatch, RegisterSchema, User
from .utils import ControllerUtils, Hasher


class UserController :

    @staticmethod
    def is_password_match(password: str, user:UserSchema) -> bool:
        algorithme = hashlib.sha256()
        algorithme.update(password.encode())

        if algorithme.hexdigest() == user.password:
            return True  # Le mot de passe est valide
        else:
            return False  # Le mot de passe est invalide
 
    @staticmethod
    def login(db: Session, email: str, password: str) -> str | None:
        _user = db.query(UserSchema).filter(UserSchema.email == email).first()
        if _user is not None :
            if not Hasher.verify_password(password, _user.password):
                return False
            else :
                return UserController.generate_token(db, email, password)

    # generate token for existant user
    @staticmethod
    def generate_token(db: Session, email: str, password: str) -> str | None:
        _user = db.query(UserSchema).filter(UserSchema.email == email).first()
        if not UserController.is_password_match(password, _user):
            return None
        token = encode({ "exp": datetime.now(tz=timezone.utc) }, SECURE_KEY, algorithm="HS256")
        _user.token = token
        db.commit()
        db.refresh(_user)
        return token

    # Get all users
    @staticmethod
    def get_all(db: Session):
        return db.query(UserSchema).all()

    # Get by token
    @staticmethod
    def get_user_by_token(db: Session, token: str) -> UserSchema :
        return db.query(UserSchema).filter(UserSchema.token == token).first()

    # Get by ID
    @staticmethod
    def get_user_by_id(db: Session, id: int) -> UserSchema :
        return db.query(UserSchema).filter(UserSchema.id == id).first()

    # Create a user
    @staticmethod
    def register(db: Session, user: RegisterSchema) -> str | None:
        hashed_password = Hasher.hash_password(user.password)

        # hashed_password = Hasher.get_password_hash(user.password)
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, user.email):
            return { 'message': "Wrong password !" }

        token = encode({ "exp": datetime.now(tz=timezone.utc) }, SECURE_KEY)
        _user = UserSchema(
            username = user.username,
            password = hashed_password,
            email = user.email,
            token = token
        )
        db.add(_user)
        db.commit()
        db.refresh(_user)
        return token

    # Full update a user
    @staticmethod
    def update_user(db: Session, user:dict, token:str) -> bool :
        _user = UserController.get_user_by_token(db, token)
        if _user == None :
            return False

        if user["email"] is not None :
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')
            if not re.fullmatch(regex, user["email"]):
                return False
            _user.email = user["email"]

        if user["password"] is not None :
            _user.password = Hasher.get_password_hash(user["password"])

        if user["username"] is not None :
            _user.username = user["username"]

        db.commit()
        db.refresh(_user)
        return True

    # Update a user
    @staticmethod
    def patch(db: Session, user: UserSchema, body: User):
        ControllerUtils.patch_entity(user, body)
        db.commit()
        db.refresh(user)
        return user

    # Delete a user
    @staticmethod
    def delete_user(db: Session, id: int) :
        _user = UserController.get_user_by_id(db, id)
        db.delete(_user)
        db.commit()
        return { 'message': "User is deleted" }



class PostController:

    @staticmethod
    def get(db: Session, post_id: int):
        return db.query(PostSchema).filter(PostSchema.id == post_id).first()

    @staticmethod
    def get_random(db: Session):
        return db.query(PostSchema).order_by(func.random()).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(PostSchema).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, post: PostCreate):
        db_post = PostSchema(
            title=post.title,
            description=post.description,
            video_url=post.video_url,
            author_id=post.author_id,
        )
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def delete(db: Session, post: PostSchema):
        db.query(PostSchema).filter(PostSchema.id == post.id).delete(synchronize_session="fetch")

    @staticmethod
    def patch(db: Session, post: PostSchema, body: PostPatch):
        ControllerUtils.patch_entity(post, body)
        db.commit()
        db.refresh(post)
        return post



class CommentController:

    @staticmethod
    def get(db: Session, comment_id: int):
        return db.query(CommentSchema).filter(CommentSchema.id == comment_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(CommentSchema).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, comment: CommentCreate):
        db_comment = CommentSchema(
            content=comment.content,
            post_id=comment.post_id,
            author_id=comment.author_id
        )
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment

    @staticmethod
    def delete(db: Session, comment: CommentSchema):
        db.query(CommentSchema).filter(CommentSchema.id == comment.id).delete(synchronize_session="fetch")

    @staticmethod
    def patch(db: Session, comment: CommentSchema, body: CommentPatch):
        ControllerUtils.patch_entity(comment, body)
        db.commit()
        db.refresh(comment)
        return comment
