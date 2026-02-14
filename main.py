from fastapi import FastAPI

app = FastAPI()

@app.get('/')
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