from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.user_schemas import UserSchema 
from ..controllers.user_controller import UserController
from ...config import get_db
from ...main import app

@app.post( "/create", schema = UserSchema )
def register(db: Session = Depends(get_db), user = UserSchema):
    return UserController.register(db = db, user = user)






