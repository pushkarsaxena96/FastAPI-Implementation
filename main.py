from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app =  FastAPI()

@app.get("/")
def index():
    return {'data':'blaog list'}

@app.get("/blog")
def index(limit:int = 10, published:bool = True, sort:Optional[str] = None):
    #Query Paramaters with Validations
    if published:
        return {'data':'blog list of published blogs'}
    else:
        return {'data':'blog list of ' + str(limit) + 'blogs'}
    

@app.get("/blog/unpublished")
def unpublished():
    #Fetch comments on blog with ID
    return {'data':"ubpub"}

@app.get("/blog/{id}")
def show(id:int):
    #Fetch blog with id
    return {'data':id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    #Fetch comments on blog with ID
    #Query Paramaters with Validations
    return {'data':{'Comments':limit}}


@app.get("/about")
def index():
    return {'data': {'name':'Saxena'}}

##############################################

class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {'data':"Blog created " + str(request.title) + " ~~ " + str(request.body)}