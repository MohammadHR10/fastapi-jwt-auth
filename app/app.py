from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from uuid import uuid4
from typing import Annotated
from .database.db import engine, get_db
from . import models, schemas
from .utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from .deps import get_current_user

# Create the FastAPI app instance
app = FastAPI(title="JWT Authentication")

@app.post('/signup', summary="Create new user", response_model=schemas.UserOut)
async def create_user(data: schemas.UserAuth, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    user = models.User(
        id=str(uuid4()),
        email=data.email,
        username=data.username,
        password=get_hashed_password(data.password)
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@app.post('/login', summary="Create access and refresh tokens for user", response_model=schemas.TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }

@app.get('/me', response_model=schemas.UserOut)
async def get_me(user: schemas.SystemUser = Depends(get_current_user)):
    return user