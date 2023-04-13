from fastapi import FastAPI
from typing import Optional

app =  FastAPI()

@app.get("/")
def index():
    return {'data':'blog list'}

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