from fastapi import FastAPI, Depends, HTTPException, status
from src.database import Base, engine, get_db
from sqlalchemy.orm import Session
import src.auth.models
from src.auth.schemas import UserCreate
import src.auth.crud as auth_crud

#create tables if they are not present
Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return auth_crud.create_user(db=db, user=user)
