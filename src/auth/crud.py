from sqlalchemy.orm import Session
from src.auth.schemas import UserCreate
from src.auth.models import User
from fastapi import HTTPException
from src.auth.hashing import create_password, verify_password

def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password, salt = create_password(user.password)
    
    new_user = User(username = user.username, hashed_password = hashed_password, salt = salt)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user