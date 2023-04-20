from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, hashing, models
from database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from routers import blog, user, authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)