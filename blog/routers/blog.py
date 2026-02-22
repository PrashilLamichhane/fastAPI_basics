from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db


router  = APIRouter()


@router.get("/blog", response_model = list[schemas.ShowBlog], tags=['blog'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
    