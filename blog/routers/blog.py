from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db


router  = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)



@router.get("/", response_model = list[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get("/{id}",response_model  = schemas.ShowBlog)
def show(id:int,  db:Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first() 
        
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
    return blog

@router.post("/",status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
