from fastapi import  HTTPException, status
from sqlalchemy.orm import Session
import models, database, schemas


def get_all(db:Session):
    blogs =db.query(models.Blog).all()
    return blogs

def create_blog(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id:int, db:Session):
    blogs =db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The requested id was not found!")
    return blogs


def destroy(id, db:Session):
    #db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    blog.delete(synchronize_session=False)
    db.commit()    
    return 'Done'

def update(id:int, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    
    blog.update(request.dict())
    db.commit()
    return 'updated'
