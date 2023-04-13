from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
def index():
    return {'data':'blog list'}

@app.get("/blog/unpublished")
def unpublished():
    #Fetch comments on blog with ID
    return {'data':"ubpub"}

@app.get("/blog/{id}")
def show(id:int):
    #Fetch blog with id
    return {'data':id}


@app.get("/blog/{id}/comments")
def comments(id):
    #Fetch comments on blog with ID
    return {'data':{'Comments':"1"}}


@app.get("/about")
def index():
    return {'data': {'name':'Saxena'}}