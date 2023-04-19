from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, hashing
from typing import List
from sqlalchemy.orm import Session


router = APIRouter()
get_db = database.get_db()

@router.post("/create_user", response_model=schemas.showUser, tags=["user"])
def create_user(request:schemas.User, db:Session=Depends(get_db)):    
    new_user = models.User(name = request.name, email = request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete("/delete_user/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["user"])
def destroy_user(id, db:Session = Depends(get_db)):
    blog = db.query(models.User).filter(models.User.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    blog.delete(synchronize_session=False)
    db.commit()    
    return 'Done'


@router.get("/user/id", response_model=schemas.showUser, tags=["user"])
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with ID:" + str(id) + " was not found!")
    return user