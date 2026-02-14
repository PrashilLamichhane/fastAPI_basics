from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def index():
    return {'data' : {'Prashil' : 'Swarnim'}}   

@app.get('/about')
def about():
    return 'HEllO'