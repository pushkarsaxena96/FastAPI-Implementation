from fastapi import APIRouter, Depends, status
import schemas, database, models
from repository import blog
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session = Depends(get_db)):    
    return blog.create_blog(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id:int, db:Session = Depends(get_db)):    
    return blog.show(id,db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog, db:Session=Depends(get_db)):
    return blog.update(id, db)