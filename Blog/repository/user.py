from fastapi import  HTTPException, status
from sqlalchemy.orm import Session
import models, database, schemas, hashing



def create_user(request:schemas.User, db:Session):    
    new_user = models.User(name = request.name, email = request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def destroy_user(id, db:Session):
    blog = db.query(models.User).filter(models.User.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    blog.delete(synchronize_session=False)
    db.commit()    
    return 'Done'

def get_user(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with ID:" + str(id) + " was not found!")
    return user