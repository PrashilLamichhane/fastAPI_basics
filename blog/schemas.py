from pydantic import BaseModel
# only for pydantic model we call it a schemas 

class Blog(BaseModel):
    title: str
    body: str
    



class ShowBlog(BaseModel):
    title : str
    class Config():
        orm_mode = True
    
