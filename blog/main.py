from fastapi import FastAPI
from . import schemas
app = FastAPI()





@app.post("/")
def create(request: schemas.Blog):
    return {"data": f"blog created with title '{request.title}' and body '{request.body}'"}