from fastapi import FastAPI
from .config import engine

#router imports
import src.routers.comment_router as comment_router
import src.routers.post_router as post_router

# models imports
import src.models.comment_model as comment_model
import src.models.post_model as post_model
import src.models.user_model as user_model

comment_model.Base.metadata.create_all(bind=engine)
post_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)

# Declare the app
app = FastAPI()

app.include_router(comment_router.router, prefix="/comment", tags=["comment"])
app.include_router(post_router.router, prefix="/post", tags=["post"])
