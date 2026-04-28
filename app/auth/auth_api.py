from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.service import signup, login
from app.auth.schema import SignupRequest, LoginRequest
from app.db.database import get_db

auth_router = APIRouter()

@auth_router.post("/register")
def register(request: SignupRequest, db: Session = Depends(get_db)):
    return signup(request, db)

@auth_router.post("/login")
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return login(request, db)