from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Union

# from . import crud, models, schemas
from .database.database import SessionLocal, engine



# Create all schemas on startup
# schemas.Base.metadata.create_all(bind=engine)

# Declare the app
app = FastAPI()



# DB session handling
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
