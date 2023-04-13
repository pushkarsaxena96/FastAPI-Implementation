from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
def index():
    return {'data':{'name':'Pushkar'}}

@app.get("/about")
def index():
    return {'data': {'name':'Saxena'}}