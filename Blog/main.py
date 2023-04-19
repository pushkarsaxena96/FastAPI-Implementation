from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, hashing, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db)):
    blogs =db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db:Session = Depends(get_db)):
    blogs =db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details" : "Block with the id "+ str(id) + " is unavailable!"}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The requested id was not found!")
    return blogs


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db)):
    #db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    blog.delete(synchronize_session=False)
    db.commit()    
    return 'Done'



@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    
    blog.update(request.dict())
    db.commit()
    return 'done'


############################### USER SECTION ###########################################



@app.post("/create_user", response_model=schemas.showUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):    
    new_user = models.User(name = request.name, email = request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.delete("/delete_user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(id, db:Session = Depends(get_db)):
    blog = db.query(models.User).filter(models.User.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    blog.delete(synchronize_session=False)
    db.commit()    
    return 'Done'


@app.get("/user/id", response_model=schemas.showUser)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with ID:" + str(id) + " was not found!")
    return user