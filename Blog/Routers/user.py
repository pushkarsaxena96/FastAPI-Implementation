from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database
from repository import user
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["User"],
    prefix="/user"
)

get_db = database.get_db

@router.post("/create_user", response_model=schemas.showUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):    
    return user.create_user(request, db)

@router.delete("/delete_user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(id:int, db:Session = Depends(get_db)):    
    return user.destroy_user(id, db)

@router.get("/id", response_model=schemas.showUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_user(id, db)