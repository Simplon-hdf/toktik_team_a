from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import engine
from .routers import CommentRouter, PostRouter, UserRouter
from .models import CommentSchema, PostSchema, UserSchema

CommentSchema.metadata.create_all(bind=engine)
PostSchema.metadata.create_all(bind=engine)
UserSchema.metadata.create_all(bind=engine)

# Declare the app
app = FastAPI()

# Open routes
app.include_router(UserRouter.router)
app.include_router(PostRouter.router)
app.include_router(CommentRouter.router)

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
