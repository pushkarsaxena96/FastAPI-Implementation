from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session


router = APIRouter()
get_db = database.get_db()

@router.get("/blog", response_model=List[schemas.ShowBlog], tags=["blogs"])
def all(db:Session = Depends(get_db)):
    blogs =db.query(models.Blog).all()
    return blogs

@router.post("/", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(request:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["blogs"])
def show(id, db:Session = Depends(get_db)):
    blogs =db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details" : "Block with the id "+ str(id) + " is unavailable!"}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The requested id was not found!")
    return blogs


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def destroy(id, db:Session = Depends(get_db)):
    #db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    blog.delete(synchronize_session=False)
    db.commit()    
    return 'Done'



@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
def update(id:int, request:schemas.Blog, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    
    blog.update(request.dict())
    db.commit()
    return 'done'