from fastapi import FastAPI

from .config import engine
from .routers import CommentRouter, PostRouter, UserRouter
from .models import CommentSchema, PostSchema, UserSchema

CommentSchema.metadata.create_all(bind=engine)
PostSchema.metadata.create_all(bind=engine)
UserSchema.metadata.create_all(bind=engine)

# Declare the app
app = FastAPI()

app.include_router(UserRouter.router)
app.include_router(PostRouter.router)
app.include_router(CommentRouter.router)

