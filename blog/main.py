from fastapi import FastAPI, Depends, status,  HTTPException


from . import schemas,models, hashing
from .database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .hashing import Hash
from .routers import blog,user
app = FastAPI()


models.Base.metadata.create_all(bind = engine)
app.include_router(blog.router)
app.include_router(user.router)



