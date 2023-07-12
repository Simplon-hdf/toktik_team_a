import hashlib
from .config import SECURE_KEY
from passlib.context import CryptContext



class ControllerUtils:

    @staticmethod
    def patch_entity(entity, new_values):
        for key, value in new_values.__dict__.items():
            setattr(entity, key, value)




class Hasher():

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # def verify_password(plain_password, hashed_password):
    #     return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def verify_password(user_password, bdd_password):
        algorithme = hashlib.sha256()
        algorithme.update(user_password.encode())

        if algorithme.hexdigest() == bdd_password:
            return True
        else:
            return False

    @staticmethod
    def hash_password(password):
        algorithme = hashlib.sha256()
        algorithme.update(password.encode())
        return algorithme.hexdigest()

    @staticmethod
    def get_password_hash(password):
        return Hasher.pwd_context.hash(password)