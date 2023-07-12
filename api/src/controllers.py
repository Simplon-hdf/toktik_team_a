from sqlalchemy.orm import Session
from .models import UserSchema, PostSchema, CommentSchema
from .dto import Hasher, UserCreate, UserSchema, PostCreate, PostPatch, CommentCreate, CommentPatch
from .utils import ControllerUtils
import jwt, re
from .config import SECURE_KEY
from datetime import datetime, timezone



class UserController :

    @staticmethod
    def get_user_by_token(db: Session, token: str) -> UserSchema :
        return db.query(UserSchema).filter(UserSchema.token == token).first()

    @staticmethod
    def is_password(password: str, user:UserSchema) -> bool:
        return Hasher.is_valid_password(password, user.password)

    @staticmethod
    def login(db: Session, email: str, password: str) -> str | None:
        _user = db.query(UserSchema).filter(UserSchema.email == email).first()
        if not UserController.is_password(db, _user):
            return None

        token = _user.token
        try :
            jwt.decode( token, SECURE_KEY, algorithms = ["HS256"] )
        except jwt.ExpiredSignatureError:
            token = UserController.generate_token(db, email, password)
        return token

    # generate token for existant user
    @staticmethod
    def generate_token(db: Session, email: str, password: str) -> str | None:
        _user = db.query(UserSchema).filter(UserSchema.email == email).first()
        if not UserController.is_password(db, _user):
            return None
        token = jwt.encode({ "exp": datetime.now(tz=timezone.utc) }, SECURE_KEY)
        _user.token = token
        db.commit()
        db.refresh(_user)
        return token

    @staticmethod
    def register(db: Session, user: UserCreate) -> str | None:
        hashed_password = Hasher.get_password_hash(user.password)
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, user.email):
            return None

        token = jwt.encode({ "exp": datetime.now(tz=timezone.utc) }, SECURE_KEY)
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

    @staticmethod
    def delete_user(db: Session, token:str) :
        _user = UserController.get_user_by_token(db, token)
        db.delete(_user)
        db.commit()
        return { 'message': "User is deleted" }



class PostController:

    @staticmethod
    def get(db: Session, post_id: int):
        return db.query(PostSchema).filter(PostSchema.id == post_id).first()

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
