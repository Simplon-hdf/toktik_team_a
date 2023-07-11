from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schemas import Hasher, UserSchema
import jwt, re
from config import SECURE_KEY
from datetime import datetime, timezone


class UserController :

    @staticmethod
    def get_user_by_token(db: Session, token: str) -> User :
        return db.query(User).filter(User.token == token).first()

    @staticmethod
    def is_password(password: str, user:User) -> bool: 
    return Hasher.is_valid_password(password, user.password)

    @staticmethod
    def login(db: Session, email: str, password: str) -> str | None:
    _user = db.query(User).filter(User.email == email).first()
    if not is_password(db, _user):
        return None

    token = _user.token
    try :
        jwt.decode( token, SECURE_KEY, algorithms = ["HS256"] )
    except jwt.ExpiredSignatureError: 
        token = generate_token(db, email, password)
    return token

    # generate token for existant user
    @staticmethod
    def generate_token(db: Session, email: str, password: str) -> str | None:
        _user = db.query(User).filter(User.email == email).first()
        if not is_password(db, _user):
            return None
        token = jwt.encode({ "exp": datetime.now(tz=timezone.utc) }, SECURE_KEY)
        _user.token = token
        db.commit()
        db.refresh(_user)
        return token

    @staticmethod
    def register(db: Session, user: UserSchema) -> str | None:
        hashed_password = Hasher.get_password_hash(user.password)
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')
    
        if not re.fullmatch(regex, user.email):
            return None
        
        token = jwt.encode({ "exp": datetime.now(tz=timezone.utc) }, SECURE_KEY)
        _user = User(
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
    _user = get_user_by_token(db, token)
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
    _user = get_user_by_token(db, token)
    db.delete(_user)
    db.commit()
    return { 'message': "User is deleted" }