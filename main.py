from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index():
    return {'data' : 'blog list'}   



@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'unpublished blog'}



@app.get('/blog/{id}')   
def about(id: int):
    return {'data' : id}




@app.get('/blog/{id}/comments')
def comment(id: int):
         return {'data' : f'blog {id} comments'}
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
   
    return {'data' : f'blog is created with title as {request.title}'}